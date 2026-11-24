#!/usr/bin/env python3
"""Status Report Comedy Sprint entry: one funny status-report line.

The program prints the line and writes it to entry.txt where the grader
looks: an explicit argument first, then MAKEFUN_OUTPUT_DIR, then /output
when it exists, and only then a file next to this script.
"""

import os
import sys

LINE = "Shipped 41 tasks this week, 0 of them the one you asked for. Still blocked on your reply from Tuesday. Morale: excellent."

# The brief caps the line at 200 characters; the program refuses to ship
# a line that breaks the cap, so a future edit cannot silently break it.
MAX_CHARS = 200


def output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return os.path.join(env, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            "status line is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS)
        )
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
