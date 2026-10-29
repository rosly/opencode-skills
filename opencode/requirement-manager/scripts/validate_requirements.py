#!/usr/bin/env python3
"""Validate mechanically observable requirements.md conventions.

This validator intentionally does not judge semantic equivalence, correctness,
feasibility, completeness, stakeholder validation, or requirement quality.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ID_TEXT = r"REQ-(?:NF-)?[A-Z][A-Z0-9]*-[0-9]+(?:\.[0-9]+)*"
ID_PATTERN = re.compile(rf"^{ID_TEXT}$")
ID_SEARCH = re.compile(ID_TEXT)
REQUIREMENT_PATTERN = re.compile(rf"^\s*-\s+({ID_TEXT}):\s*(.*)$")
REQUIREMENT_CANDIDATE_PATTERN = re.compile(r"^\s*-\s+REQ(?:-NF)?-")
IMPLEMENTATION_REFERENCE_PATTERN = re.compile(
    r"(?:\b[\w.-]+\.(?:py|js|jsx|ts|tsx|go|rs|java|cs|c|cc|cpp|h|hpp|sh)\b|"
    r"\b[\w./-]+#[A-Za-z_]\w*\b|::[A-Za-z_]\w*|\b[A-Za-z_]\w*\(\))",
    re.IGNORECASE,
)
PROVENANCE_COLUMNS = (
    "requirement id",
    "source or parent",
    "rationale",
    "decision authority",
)
LIFECYCLE_COLUMNS = ("previous id", "disposition", "successor", "reason")
LIFECYCLE_DISPOSITIONS = {
    "clarified",
    "replaced",
    "relocated",
    "split",
    "merged",
    "retired",
}


@dataclass(frozen=True)
class Requirement:
    identifier: str
    wording: str
    path: Path
    line: int


@dataclass(frozen=True)
class Table:
    columns: tuple[str, ...]
    rows: tuple[tuple[int, tuple[str, ...]], ...]


def parse_identifier(identifier: str) -> tuple[str, tuple[int, ...]]:
    prefix, numbers = identifier.rsplit("-", 1)
    return prefix, tuple(int(part) for part in numbers.split("."))


def parse_table(lines: list[str], header_index: int) -> Table:
    columns = tuple(cell.strip().lower() for cell in lines[header_index].strip().strip("|").split("|"))
    rows: list[tuple[int, tuple[str, ...]]] = []
    for index in range(header_index + 2, len(lines)):
        if not lines[index].lstrip().startswith("|"):
            break
        cells = tuple(cell.strip() for cell in lines[index].strip().strip("|").split("|"))
        if len(cells) != len(columns):
            break
        rows.append((index + 1, cells))
    return Table(columns=columns, rows=tuple(rows))


def find_table(lines: list[str], expected_columns: tuple[str, ...]) -> Table | None:
    for index, line in enumerate(lines[:-1]):
        columns = tuple(cell.strip().lower() for cell in line.strip().strip("|").split("|"))
        if columns == expected_columns and lines[index + 1].lstrip().startswith("|"):
            return parse_table(lines, index)
    return None


def has_natural_number_format(identifier: str) -> bool:
    return all(part.isdigit() and int(part) > 0 and str(int(part)) == part for part in identifier.rsplit("-", 1)[1].split("."))


def is_blank_cell(value: str) -> bool:
    return value.strip().lower() in {"", "-", "—", "none", "n/a"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate deterministic requirements.md conventions.")
    parser.add_argument("paths", nargs="+", type=Path, help="Applicable requirements.md files to validate together")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    requirements: list[Requirement] = []
    provenance_tables: dict[Path, Table | None] = {}
    lifecycle_tables: dict[Path, Table | None] = {}

    for path in args.paths:
        if not path.is_file():
            errors.append(f"{path}: file does not exist")
            continue
        if path.name.lower() != "requirements.md":
            warnings.append(f"{path}: filename is not requirements.md")

        lines = path.read_text(encoding="utf-8").splitlines()
        provenance_tables[path] = find_table(lines, PROVENANCE_COLUMNS)
        lifecycle_tables[path] = find_table(lines, LIFECYCLE_COLUMNS)

        for line_number, line in enumerate(lines, start=1):
            match = REQUIREMENT_PATTERN.match(line)
            if match is None:
                if REQUIREMENT_CANDIDATE_PATTERN.match(line):
                    errors.append(f"{path}:{line_number}: malformed requirement declaration")
                continue
            identifier, wording = match.groups()
            requirements.append(Requirement(identifier, wording, path, line_number))
            if not ID_PATTERN.fullmatch(identifier):
                errors.append(f"{path}:{line_number}: invalid requirement ID: {identifier}")
            if not has_natural_number_format(identifier):
                errors.append(f"{path}:{line_number}: ID must use positive natural numbers without zero padding: {identifier}")
            if " shall " not in f" {wording.lower()} ":
                warnings.append(f"{path}:{line_number}: normative wording contains no 'shall': {identifier}")
            if IMPLEMENTATION_REFERENCE_PATTERN.search(wording):
                warnings.append(f"{path}:{line_number}: possible implementation reference in normative wording: {identifier}")

    active_by_id: dict[str, Requirement] = {}
    for requirement in requirements:
        if requirement.identifier in active_by_id:
            errors.append(
                f"{requirement.path}:{requirement.line}: duplicate active ID {requirement.identifier}; "
                f"first declared at {active_by_id[requirement.identifier].path}:{active_by_id[requirement.identifier].line}"
            )
        else:
            active_by_id[requirement.identifier] = requirement

    last_path_by_namespace: dict[str, tuple[int, ...]] = {}
    for requirement in requirements:
        namespace, number_path = parse_identifier(requirement.identifier)
        if namespace in last_path_by_namespace and number_path < last_path_by_namespace[namespace]:
            errors.append(
                f"{requirement.path}:{requirement.line}: {requirement.identifier} is out of top-to-bottom "
                f"hierarchical order for {namespace}"
            )
        last_path_by_namespace[namespace] = number_path

    provenance_ids: set[str] = set()
    for path, table in provenance_tables.items():
        if table is None:
            errors.append(f"{path}: missing required provenance table with columns: {' | '.join(PROVENANCE_COLUMNS)}")
            continue
        for line_number, row in table.rows:
            identifier, source, rationale, authority = row
            if not ID_PATTERN.fullmatch(identifier):
                errors.append(f"{path}:{line_number}: invalid provenance requirement ID: {identifier}")
                continue
            if not has_natural_number_format(identifier):
                errors.append(f"{path}:{line_number}: provenance ID must use positive natural numbers without zero padding: {identifier}")
            if identifier in provenance_ids:
                errors.append(f"{path}:{line_number}: duplicate provenance row: {identifier}")
            provenance_ids.add(identifier)
            if identifier not in active_by_id:
                errors.append(f"{path}:{line_number}: provenance refers to non-active requirement: {identifier}")
            if is_blank_cell(source):
                errors.append(f"{path}:{line_number}: provenance source or parent is required: {identifier}")
            if is_blank_cell(authority):
                errors.append(f"{path}:{line_number}: provenance decision authority is required: {identifier}")
            if is_blank_cell(rationale):
                warnings.append(f"{path}:{line_number}: blank rationale requires manual confirmation that derivation is self-evident: {identifier}")

    for identifier, requirement in active_by_id.items():
        if identifier not in provenance_ids:
            errors.append(f"{requirement.path}:{requirement.line}: active requirement lacks provenance: {identifier}")

    lifecycle_previous: dict[str, tuple[str, Path, int]] = {}
    superseded_ids: set[str] = set()
    for path, table in lifecycle_tables.items():
        if table is None:
            errors.append(f"{path}: missing required lifecycle table with columns: {' | '.join(LIFECYCLE_COLUMNS)}")
            continue
        for line_number, row in table.rows:
            previous_cell, disposition, successor_cell, reason = row
            previous_ids = ID_SEARCH.findall(previous_cell)
            successor_ids = ID_SEARCH.findall(successor_cell)
            normalized_disposition = disposition.strip().lower()
            if not previous_ids:
                errors.append(f"{path}:{line_number}: lifecycle row has no previous requirement ID")
                continue
            for identifier in [*previous_ids, *successor_ids]:
                if not has_natural_number_format(identifier):
                    errors.append(
                        f"{path}:{line_number}: lifecycle ID must use positive natural numbers without zero padding: {identifier}"
                    )
            if normalized_disposition not in LIFECYCLE_DISPOSITIONS:
                errors.append(f"{path}:{line_number}: unsupported lifecycle disposition: {disposition}")
            if is_blank_cell(reason):
                errors.append(f"{path}:{line_number}: lifecycle reason is required")
            for identifier in previous_ids:
                if identifier in lifecycle_previous:
                    errors.append(f"{path}:{line_number}: duplicate lifecycle entry for previous ID: {identifier}")
                lifecycle_previous[identifier] = (normalized_disposition, path, line_number)
                if normalized_disposition == "clarified":
                    if identifier not in active_by_id:
                        errors.append(f"{path}:{line_number}: clarified ID must remain active: {identifier}")
                else:
                    superseded_ids.add(identifier)
                    if identifier in active_by_id:
                        errors.append(f"{path}:{line_number}: non-clarified previous ID remains active: {identifier}")
            if normalized_disposition == "retired" and successor_ids:
                errors.append(f"{path}:{line_number}: retired lifecycle row must not name a successor")
            if normalized_disposition not in {"retired", "clarified"} and not successor_ids:
                errors.append(f"{path}:{line_number}: {disposition} lifecycle row requires a successor")
            for identifier in successor_ids:
                if identifier not in active_by_id:
                    errors.append(f"{path}:{line_number}: lifecycle successor is not active: {identifier}")

    for requirement in requirements:
        for referenced_id in ID_SEARCH.findall(requirement.wording):
            if referenced_id == requirement.identifier:
                continue
            if referenced_id in superseded_ids:
                errors.append(
                    f"{requirement.path}:{requirement.line}: active requirement {requirement.identifier} "
                    f"references superseded or retired ID {referenced_id}"
                )
            elif referenced_id not in active_by_id:
                warnings.append(
                    f"{requirement.path}:{requirement.line}: reference {referenced_id} was not found in supplied files"
                )

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Validated {len(requirements)} active requirements across {len(args.paths)} file(s): {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
