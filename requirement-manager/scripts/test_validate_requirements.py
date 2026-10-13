#!/usr/bin/env python3
"""Regression tests for validate_requirements.py."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR = Path(__file__).with_name("validate_requirements.py")


def document(requirements: str, provenance: str, lifecycle: str = "") -> str:
    return f"""# Example Requirements

## 1. Scope

Module abbreviation: `MOD`.

## 2. Functional requirements

{requirements}

## 3. Non-functional requirements

## 4. Decided exclusions

## 5. Requirement provenance

| Requirement ID | Source or parent | Rationale | Decision authority |
|---|---|---|---|
{provenance}

## 6. Requirement lifecycle map

| Previous ID | Disposition | Successor | Reason |
|---|---|---|---|
{lifecycle}
"""


class ValidatorTests(unittest.TestCase):
    def run_validator(self, content: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "requirements.md"
            path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATOR), str(path)],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_accepts_valid_document(self) -> None:
        result = self.run_validator(document(
            "- REQ-MOD-1.1: When an accepted request is received, the service shall return an acknowledgment containing the request identifier.\n"
            "- REQ-MOD-1.2: When a request lacks an identifier, the service shall return a rejection containing the rejection reason.",
            "| REQ-MOD-1.1 | DEC-1 | Establish acknowledgment | Product owner |\n"
            "| REQ-MOD-1.2 | DEC-2 | Reject invalid input | Product owner |",
        ))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_zero_padding_and_missing_provenance(self) -> None:
        result = self.run_validator(document(
            "- REQ-MOD-01.1: The service shall return an acknowledgment.\n"
            "- REQ-MOD-2.1: The service shall return a rejection.",
            "| REQ-MOD-2.1 | DEC-2 | Reject invalid input | Product owner |",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("without zero padding", result.stdout)
        self.assertIn("lacks provenance", result.stdout)

    def test_rejects_duplicate_and_out_of_order_active_ids(self) -> None:
        result = self.run_validator(document(
            "- REQ-MOD-2.1: The service shall return an acknowledgment.\n"
            "- REQ-MOD-1.1: The service shall return a rejection.\n"
            "- REQ-MOD-1.1: The service shall retain the rejection reason.",
            "| REQ-MOD-2.1 | DEC-1 | Establish acknowledgment | Product owner |\n"
            "| REQ-MOD-1.1 | DEC-2 | Reject invalid input | Product owner |",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate active ID", result.stdout)
        self.assertIn("out of top-to-bottom hierarchical order", result.stdout)

    def test_rejects_active_previous_id_and_reference_to_superseded_id(self) -> None:
        result = self.run_validator(document(
            "- REQ-MOD-1.1: The service shall return an acknowledgment.\n"
            "- REQ-MOD-2.1: The service shall satisfy REQ-MOD-1.1.",
            "| REQ-MOD-1.1 | DEC-1 | Original acknowledgment | Product owner |\n"
            "| REQ-MOD-2.1 | REQ-MOD-1.1 | Replace acknowledgment | Product owner |",
            "| REQ-MOD-1.1 | Replaced | REQ-MOD-2.1 | Observable response changed |",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("previous ID remains active", result.stdout)
        self.assertIn("references superseded or retired ID", result.stdout)

    def test_rejects_malformed_requirement_declaration(self) -> None:
        result = self.run_validator(document(
            "- REQ-mod-1.1: The service shall return an acknowledgment.",
            "",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("malformed requirement declaration", result.stdout)


if __name__ == "__main__":
    unittest.main()
