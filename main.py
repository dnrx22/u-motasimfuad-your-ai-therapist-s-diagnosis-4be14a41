#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — one line, written to entry.txt.

Deterministic: writes the exact same bytes on every run.
Stdlib only. No network.
"""

import os

LINE = (
    "Diagnosis: compulsive apology disorder \u2014 patient apologises "
    "to the chatbot, then apologises for apologising."
)

MAX_CHARS = 200
MAX_WORDS = 20


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "line is %d words, over the %d limit" % (len(words), MAX_WORDS)
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # Terminate the file with a newline so entry.txt is a well-formed
        # POSIX text file (the line itself stays a single line).
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
