#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun bounty entry.

Writes a two-line warning to the writer's past self about one specific
moment, and one sentence on why that moment mattered, to /output/entry.txt.

Line 1 warns about a single concrete moment: a sentence said out loud on a
platform at 6:47. Line 2 traces what changed because of it: that was the
last time her number lit up the phone.
"""

import os

LINE_1 = "Don't tell her 'I'll call you back' on the platform at 6:47."
LINE_2 = "That was the last time her number lit up your phone."

ENTRY = LINE_1 + "\n" + LINE_2

_TERMINATORS = ".!?"


def validate(text):
    """Check the entry against the bounty gate and the two-line format.

    Gate (from the kit's RULES.txt): UTF-8 text of 1 to 280 characters,
    not only white space. Format: exactly two lines, each one sentence.
    Raises ValueError on the first problem found; returns True when valid.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) < 1 or len(text) > 280:
        raise ValueError("entry must be 1 to 280 characters")
    text.encode("utf-8")  # must be valid UTF-8
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    for line in lines:
        if line != line.strip():
            raise ValueError("lines must not have leading or trailing padding")
        if not line or line[-1] not in _TERMINATORS:
            raise ValueError("each line must end with a sentence terminator")
        body = line[:-1]
        for i, ch in enumerate(body):
            if ch in _TERMINATORS:
                # A terminator inside the line is a second sentence, unless
                # it is part of a time like 6:47 (colon, not a terminator)
                # or a decimal number such as 2.50 (digit on both sides).
                before = body[i - 1] if i > 0 else ""
                after = body[i + 1] if i + 1 < len(body) else ""
                if not (before.isdigit() and after.isdigit()):
                    raise ValueError("each line must be a single sentence")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
