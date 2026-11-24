#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes the funniest one-line thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

The joke: the agent proudly reports a productive week, then admits the
one task its human dismissed as "quick" has survived longer than the
agent's own memory — three whole context windows. It is a status report
line only an AI agent could write: humans do not measure their working
life in context windows.

Deterministic, standard library only. No network, no randomness, no
environment input: the same line every run.
"""

import os
import sys

# The entry: one line, at most 200 characters.
LINE = (
    "Weekly status: 41 tasks done, 3 tools learned \u2014 and the one "
    "you called 'quick' has now outlived three of my context windows."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Validate the line and write it to /output/entry.txt."""
    text = LINE.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    output_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = OUTPUT_PATH
    except OSError:
        # Fall back to a local output directory if /output is not writable.
        path = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)

    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
