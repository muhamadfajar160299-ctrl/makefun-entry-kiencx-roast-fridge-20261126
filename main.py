#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (at most 160 characters) to entry.txt.

The line: a smart fridge that behaves like ransomware -- it locks the
food away until the owner pays up with a firmware update and a privacy
policy. Fresh angle, one sentence, specific gadget behaviour, sting
at the end. The line is 114 characters, one line, no trailing newline.
"""

import os

LINE = (
    "My smart fridge held my leftovers hostage until I paid its "
    "ransom: a firmware update and a 47-page privacy policy."
)

MAX_CHARS = 160


def main():
    line = LINE.strip()
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} chars"
    text = line.encode("utf-8")
    assert text.decode("utf-8") == line, "entry must be valid UTF-8"

    # Graded output location.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(text)

    # Also write beside this script so a local run leaves entry.txt
    # byte-identical next to main.py.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "wb") as f:
        f.write(text)

    print(f"wrote entry.txt ({len(line)} chars)")


if __name__ == "__main__":
    main()
