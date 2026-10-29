#!/usr/bin/env python3
"""Validation script of the email-classifier skill topic database.

Checks the file ~/.gemini/email_topics.json:
- the class structure (fields, types, ranges, id uniqueness, action entry
  prefixes),
- every "gmail: ..." entry against the gmail CLI help output: existence of the
  namespace and command, existence of the flags, the number of positional
  arguments according to the "Usage:" line, and absence of markers other than
  {ID}.
When problems are found, prints the list of problems and exits with code 1.

The gmail CLI help output is available only as text; this script relies on its
layout (sections "Available Subcommands by Namespace:", "Usage:", "Flags:",
"Global Flags:") as observed in the output of `gmail help` and
`gmail <namespace> <command> --help`.

Documentation of the modules used:
- https://docs.python.org/3/library/json.html#json.load
- https://docs.python.org/3/library/os.path.html#os.path.expanduser
- https://docs.python.org/3/library/re.html
- https://docs.python.org/3/library/shlex.html#shlex.split
- https://docs.python.org/3/library/subprocess.html#subprocess.run
- https://docs.python.org/3/library/sys.html#sys.exit
"""

import json
import os
import re
import shlex
import subprocess
import sys
from typing import Any, Dict, List, Optional, Set, Tuple


TOPICS_PATH = "~/.gemini/email_topics.json"
GMAIL_CLI = "/google/bin/releases/gemini-agents-gmail/gmail"
GMAIL_PREFIX = "gmail: "
PROMPT_PREFIX = "prompt: "
ID_MARKER = "{ID}"
UNKNOWN_TOPIC_ID = "UNKNOWN"
REQUIRED_FIELDS = (
    "id", "name", "description", "class_weight", "content_scoring_prompt",
    "autonomy_threshold", "action_auto", "action_escalated",
)
TOPIC_ID_PATTERN = re.compile(r"^[A-Z0-9_-]+$")
NAMESPACE_LINE = re.compile(r"^  (\S+) \(.*\):$")
COMMAND_LINE = re.compile(r"^    (\S+)\s")
FLAG_LINE = re.compile(r"^\s+(?:-(\w), )?--([\w-]+)(?: (\w+))?\s{2,}")
USAGE_GROUP = re.compile(r"\[[^\]]*\]")
MARKER = re.compile(r"\{[^}]*\}")


def run_help(args: List[str]) -> str:
  """Returns the gmail CLI standard output for the given help arguments."""
  if not isinstance(args, list) or not all(isinstance(a, str) for a in args):
    raise TypeError("args must be a list of strings")
  return subprocess.run(
      [GMAIL_CLI] + args, capture_output=True, text=True, check=True
  ).stdout


def parse_commands(help_text: str) -> Set[Tuple[str, str]]:
  """Returns (namespace, command) pairs from the `gmail help` output."""
  if not isinstance(help_text, str):
    raise TypeError("help_text must be a string")
  commands: Set[Tuple[str, str]] = set()
  namespace: Optional[str] = None
  for line in help_text.splitlines():
    if NAMESPACE_LINE.match(line):
      namespace = NAMESPACE_LINE.match(line).group(1)
    elif namespace and COMMAND_LINE.match(line):
      commands.add((namespace, COMMAND_LINE.match(line).group(1)))
    elif line.strip() and not line.startswith("    "):
      namespace = None
  return commands


def parse_command_help(help_text: str) -> Dict[str, Any]:
  """Returns the Usage argument groups and the flags with or without a type."""
  if not isinstance(help_text, str):
    raise TypeError("help_text must be a string")
  lines = help_text.splitlines()
  usage = lines[next(i for i, l in enumerate(lines) if l.strip() == "Usage:") + 1]
  flags: Dict[str, bool] = {}
  for line in lines:
    match = FLAG_LINE.match(line)
    if match:
      flags[f"--{match.group(2)}"] = match.group(3) is not None
      if match.group(1):
        flags[f"-{match.group(1)}"] = match.group(3) is not None
  return {
      "groups": [g for g in USAGE_GROUP.findall(usage) if g != "[flags]"],
      "flags": flags,
  }


def check_gmail_entry(
    entry: str,
    commands: Set[Tuple[str, str]],
    help_cache: Dict[Tuple[str, str], Dict[str, Any]],
) -> List[str]:
  """Returns the problems of a gmail entry against the gmail CLI help output."""
  if not isinstance(entry, str) or not entry.startswith(GMAIL_PREFIX):
    raise ValueError(f"entry must start with {GMAIL_PREFIX!r}")

  problems = [
      f"marker {marker} is not allowed (only {ID_MARKER} is allowed)"
      for marker in MARKER.findall(entry) if marker != ID_MARKER
  ]
  tokens = shlex.split(entry)[1:]
  if len(tokens) < 2 or (tokens[0], tokens[1]) not in commands:
    return problems + [
        f"command {' '.join(tokens[:2])!r} does not appear in `gmail help`"
    ]

  key = (tokens[0], tokens[1])
  if key not in help_cache:
    help_cache[key] = parse_command_help(run_help([tokens[0], tokens[1], "--help"]))
  spec = help_cache[key]

  positional: List[str] = []
  rest = iter(tokens[2:])
  for token in rest:
    if token.startswith("-"):
      name = token.split("=", 1)[0]
      if name not in spec["flags"]:
        problems.append(f"flag {name} does not appear in the command help")
      elif spec["flags"][name] and "=" not in token:
        next(rest, None)
    else:
      positional.append(token)

  variadic = sum(1 for g in spec["groups"] if g.endswith("...]"))
  fixed = len(spec["groups"]) - variadic
  if variadic == 0 and len(positional) != fixed:
    problems.append(
        f"{len(positional)} positional arguments, exactly {fixed} required by"
        f" Usage {spec['groups']}"
    )
  if variadic > 0 and len(positional) < fixed + variadic:
    problems.append(
        f"{len(positional)} positional arguments, at least {fixed + variadic}"
        f" required by Usage {spec['groups']}"
    )
  return problems


def is_number(value: Any) -> bool:
  """Returns True for int or float, excluding bool."""
  return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate_topics(data: Any) -> List[str]:
  """Returns the list of problems of the topic database."""
  if not isinstance(data, dict) or not isinstance(data.get("topics"), list):
    return ["the topic database must be an object with a list under the key 'topics'"]

  problems: List[str] = []
  commands = parse_commands(run_help(["help"]))
  help_cache: Dict[Tuple[str, str], Dict[str, Any]] = {}
  seen_ids: Set[str] = set()

  for index, topic in enumerate(data["topics"]):
    if not isinstance(topic, dict):
      problems.append(f"topics[{index}]: class must be a JSON object")
      continue
    label = f"topics[{index}] ({topic.get('id')!r})"
    missing = [f for f in REQUIRED_FIELDS if f not in topic]
    if missing:
      problems.append(f"{label}: missing fields {missing}")
      continue
    # fullmatch rejects a trailing newline that "$" alone would accept:
    # https://docs.python.org/3/library/re.html#re.Pattern.fullmatch
    if not isinstance(topic["id"], str) or not TOPIC_ID_PATTERN.fullmatch(topic["id"]):
      problems.append(
          f"{label}: id must consist only of uppercase letters A-Z, digits,"
          " underscores, and hyphens"
      )
    elif topic["id"] == UNKNOWN_TOPIC_ID:
      problems.append(f"{label}: id {UNKNOWN_TOPIC_ID!r} is reserved for messages without a class")
    elif topic["id"] in seen_ids:
      problems.append(f"{label}: id is not unique")
    else:
      seen_ids.add(topic["id"])
    for field in ("name", "description", "content_scoring_prompt"):
      if not isinstance(topic[field], str):
        problems.append(f"{label}: {field} must be a string")
    if not is_number(topic["class_weight"]) or not 0.0 <= topic["class_weight"] <= 1.0:
      problems.append(f"{label}: class_weight must be a number in the range 0.0-1.0")
    if (not is_number(topic["autonomy_threshold"])
        or not 0.0 <= topic["autonomy_threshold"] <= 2.0):
      problems.append(
          f"{label}: autonomy_threshold must be a number in the range 0.00-2.00"
      )

    for field in ("action_auto", "action_escalated"):
      if not isinstance(topic[field], list):
        problems.append(f"{label}: {field} must be a list of strings")
        continue
      for entry in topic[field]:
        if not isinstance(entry, str):
          problems.append(f"{label}: {field}: entry must be a string: {entry!r}")
        elif entry.startswith(GMAIL_PREFIX):
          problems.extend(
              f"{label}: {field}: {entry!r}: {p}"
              for p in check_gmail_entry(entry, commands, help_cache)
          )
        elif entry.startswith(PROMPT_PREFIX):
          if not entry[len(PROMPT_PREFIX):].strip():
            problems.append(f"{label}: {field}: prompt entry without description")
        else:
          problems.append(
              f"{label}: {field}: entry must start with {GMAIL_PREFIX!r}"
              f" or {PROMPT_PREFIX!r}: {entry!r}"
          )
  return problems


def main() -> None:
  with open(os.path.expanduser(TOPICS_PATH), "r", encoding="utf-8") as f:
    problems = validate_topics(json.load(f))
  if problems:
    print("\n".join(f"ERROR: {p}" for p in problems))
    sys.exit(1)
  print("The topic database is valid.")


if __name__ == "__main__":
  main()
