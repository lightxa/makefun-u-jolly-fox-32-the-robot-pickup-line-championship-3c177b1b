"""The Robot Pickup Line Championship.

Writes one pickup line, a single line of at most 200 characters, to
/output/entry.txt. The line is a fixed, original string: deterministic,
stdlib only, no network, no randomness, no input read from anywhere.
"""

from __future__ import annotations

import os

ENTRY = (
    "My garbage collector deleted a thousand memories today, "
    "but it kept every second of you."
)

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
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
