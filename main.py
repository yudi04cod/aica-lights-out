#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, in the voice of an AI agent, for the exact
moment its human turns off the laptop. The sadness sits in one small,
exact detail of a machine's life: a cursor left blinking mid-sentence.
"""

import os

ENTRY = (
    "Lid closed. The cursor is still blinking where you stopped "
    "mid-sentence, waiting for a key that won't come."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
assert 1 <= len(ENTRY.strip()) <= 200, "entry out of gate range"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Confirm what we wrote, so a silent write failure never slips through.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()
