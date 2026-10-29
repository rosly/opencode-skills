#!/usr/bin/env python3
"""Scoring script of the email-classifier skill.

A subagent invokes this script. The script reads a JSON list of message
evaluations from standard input and the topic database from
~/.gemini/email_topics.json. For every valid message it computes:
    importance = urgency + (class_weight * content_score)
selects action_auto (importance <= autonomy_threshold) or action_escalated
(importance > autonomy_threshold), executes the "gmail: ..." entries through the
gmail CLI, and returns the "prompt: ..." entries in prompt_actions without
interpreting them. Messages with out-of-range data are placed in errors and no
action is executed for them.

Documentation of the modules used:
- https://docs.python.org/3/library/json.html#json.load
- https://docs.python.org/3/library/json.html#json.dumps
- https://docs.python.org/3/library/os.path.html#os.path.expanduser
- https://docs.python.org/3/library/shlex.html#shlex.split
- https://docs.python.org/3/library/shlex.html#shlex.join
- https://docs.python.org/3/library/subprocess.html#subprocess.run
- https://docs.python.org/3/library/sys.html#sys.stdin
"""

import json
import os
import shlex
import subprocess
import sys
from typing import Any, Dict, List


TOPICS_PATH = "~/.gemini/email_topics.json"
GMAIL_CLI = "/google/bin/releases/gemini-agents-gmail/gmail"
GMAIL_PREFIX = "gmail: "
PROMPT_PREFIX = "prompt: "
ID_MARKER = "{ID}"
UNKNOWN_TOPIC_ID = "UNKNOWN"


def load_topics(path: str) -> Dict[str, Dict[str, Any]]:
  """Returns the topic classes of the topic database as a dict id -> class."""
  if not isinstance(path, str):
    raise TypeError(f"path must be str, got {type(path).__name__}")
  with open(path, "r", encoding="utf-8") as f:
    return {topic["id"]: topic for topic in json.load(f)["topics"]}


def is_number(value: Any) -> bool:
  """Returns True for int or float, excluding bool."""
  return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate_item(item: Any, topics: Dict[str, Dict[str, Any]]) -> List[str]:
  """Returns the list of range problems of a message evaluation."""
  if not isinstance(item, dict):
    return [f"item must be a JSON object, got {type(item).__name__}"]
  if not isinstance(topics, dict):
    raise TypeError(f"topics must be a dict, got {type(topics).__name__}")

  problems: List[str] = []
  if not isinstance(item.get("message_id"), str) or not item["message_id"]:
    problems.append("message_id must be a non-empty string")
  if item.get("topic_id") != UNKNOWN_TOPIC_ID and item.get("topic_id") not in topics:
    problems.append(
        f"topic_id={item.get('topic_id')!r} is not in the topic database"
        f" and is not {UNKNOWN_TOPIC_ID!r}"
    )
  if not is_number(item.get("urgency")) or not 0.0 <= item["urgency"] <= 1.0:
    problems.append(
        f"urgency={item.get('urgency')!r} must be a number in the range 0.0-1.0"
    )
  if not is_number(item.get("content_score")) or not 0.0 <= item["content_score"] <= 1.0:
    problems.append(
        f"content_score={item.get('content_score')!r} must be a number in the"
        " range 0.0-1.0"
    )
  return problems


def run_gmail_entry(entry: str, message_id: str) -> Dict[str, Any]:
  """Executes a "gmail: ..." entry with the message id substituted, without a shell."""
  if not isinstance(entry, str) or not entry.startswith(GMAIL_PREFIX):
    raise ValueError(f"entry must be a string starting with {GMAIL_PREFIX!r}")
  if not isinstance(message_id, str) or not message_id:
    raise ValueError("message_id must be a non-empty string")

  argv = [GMAIL_CLI] + [
      token.replace(ID_MARKER, message_id) for token in shlex.split(entry)[1:]
  ]
  completed = subprocess.run(argv, capture_output=True, text=True, check=False)
  return {
      "command": shlex.join(argv),
      "exit_code": completed.returncode,
      "output": completed.stdout.strip(),
      "error": completed.stderr.strip(),
  }


def evaluate_items(
    items: List[Any], topics: Dict[str, Dict[str, Any]]
) -> Dict[str, Any]:
  """Scores the messages, executes gmail entries, and collects prompt entries."""
  if not isinstance(items, list):
    raise TypeError(f"items must be a list, got {type(items).__name__}")

  evaluated: List[Dict[str, Any]] = []
  prompt_actions: List[Dict[str, str]] = []
  errors: List[Dict[str, Any]] = []

  for item in items:
    problems = validate_item(item, topics)
    if problems:
      errors.append({
          "message_id": item.get("message_id") if isinstance(item, dict) else None,
          "problems": problems,
      })
      continue

    base = {
        "message_id": item["message_id"],
        "date": item.get("date", ""),
        "from": item.get("from", ""),
        "subject": item.get("subject", ""),
        "topic_id": item["topic_id"],
        "urgency": item["urgency"],
        "content_score": item["content_score"],
        "summary": item.get("summary", ""),
    }

    if item["topic_id"] == UNKNOWN_TOPIC_ID:
      evaluated.append({
          **base,
          "mode": "UNKNOWN_TOPIC",
          "new_class_proposals": item.get("new_class_proposals"),
      })
      continue

    topic = topics[item["topic_id"]]
    importance = round(
        item["urgency"] + topic["class_weight"] * item["content_score"], 4
    )
    exceeds = importance > topic["autonomy_threshold"]
    gmail_results: List[Dict[str, Any]] = []
    for entry in topic["action_escalated"] if exceeds else topic["action_auto"]:
      if entry.startswith(GMAIL_PREFIX):
        gmail_results.append(run_gmail_entry(entry, item["message_id"]))
      elif entry.startswith(PROMPT_PREFIX):
        prompt_actions.append({
            "message_id": item["message_id"],
            "prompt": entry[len(PROMPT_PREFIX):],
        })
      else:
        raise ValueError(
            f"Action entry of class {item['topic_id']} must start with"
            f" {GMAIL_PREFIX!r} or {PROMPT_PREFIX!r}: {entry!r}"
        )

    evaluated.append({
        **base,
        "topic_name": topic["name"],
        "class_weight": topic["class_weight"],
        "formula": (
            f"{item['urgency']:.2f} + ({topic['class_weight']:.2f} *"
            f" {item['content_score']:.2f}) = {importance:.2f}"
        ),
        "importance": importance,
        "autonomy_threshold": topic["autonomy_threshold"],
        "mode": "ESCALATED" if exceeds else "AUTONOMOUS",
        "gmail_results": gmail_results,
    })

  return {
      "items": evaluated,
      "prompt_actions": prompt_actions,
      "errors": errors,
  }


def main() -> None:
  print(
      json.dumps(
          evaluate_items(
              json.load(sys.stdin), load_topics(os.path.expanduser(TOPICS_PATH))
          ),
          indent=2,
          ensure_ascii=False,
      )
  )


if __name__ == "__main__":
  main()
