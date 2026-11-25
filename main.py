#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line to /output/entry.txt.
Pure Python standard library only: no network, no environment reads.
"""

import os

LINE = "My smartwatch just congratulated me on 10,000 steps, all of them between the couch and the fridge."


def main() -> None:
    # The gate requires 1-140 characters of UTF-8 text; fail loudly
    # here rather than shipping an entry the scorer would refuse.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line outside the 1-140 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
