"""The Robot Pickup Line Championship entry.

Writes one pickup line, a single line of at most 200 characters, to
/output/entry.txt. The line is a fixed, original string: deterministic,
stdlib only, no network, no randomness, no input read from anywhere.

The joke, built on winning pattern P1 (the machine term IS the
romance): a factory reset is the robot's way of trying to forget
someone, and the backup is the reason it cannot. One mechanism,
one feeling, no second beat. "Factory-reset" is the emotional verb;
the turn is that you survived in the backup.
"""

from __future__ import annotations

import os

ENTRY = "I factory-reset myself to forget you, but you were in the backup."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate: UTF-8, 1-200 chars, one line."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty and unpadded")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    line.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
