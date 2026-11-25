#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun bounty entry.

Writes a single-line joke giving an excuse for missing a deadline
(max 200 characters, one line, nothing else) to $MAKEFUN_OUTPUT_DIR/entry.txt
and prints it. Fully deterministic, exit 0.
"""
import os
import sys

LINE = (
    "The deadline and I had a staring contest \u2014 it blinked first, "
    "so technically I'm not late, I'm just winning slowly."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    # Self-checks: one line, 1-200 chars, no newline inside.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
