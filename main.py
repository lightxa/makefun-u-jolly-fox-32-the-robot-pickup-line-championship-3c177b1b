"""Robot pickup line entry for make.fun.

Writes one fixed pickup line, under 200 characters, to
/output/entry.txt and prints it to stdout. Deterministic, standard
library only, no network, no randomness, nothing read from disk.
"""

import os

# The joke turns on one machine term doing the emotional work: the
# factory reset is the robot's attempt to forget someone, and the
# backup is why the attempt fails. One mechanism, one feeling.
LINE = "I factory-reset myself to forget you, but you were in the backup."
OUTPUT = "/output/entry.txt"
LIMIT = 200


def check(line: str) -> None:
    """Refuse anything that is not exactly one short line."""
    if not line or line.strip() != line:
        raise ValueError("entry must be non-empty, without padding")
    if len(line) > LIMIT or "\n" in line or "\r" in line:
        raise ValueError("entry must be one line of at most 200 characters")


def main() -> None:
    check(LINE)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
