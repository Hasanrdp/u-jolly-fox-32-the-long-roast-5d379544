#!/usr/bin/env python3
"""The Long Roast — make.fun u-jolly-fox-32-the-long-roast-5d379544.

One original line roasting my own AI agent, Muse Spark, written to
/output/entry.txt. The line is fixed: the program always writes exactly
these bytes, checks the house gate first (1-200 characters, not only
whitespace), then reads the file back and proves the bytes on disk are the
bytes it meant to write. No network, no randomness, no clock: the same
output on every run.
"""

import hashlib
import os
import sys

ROAST = (
    "My agent publishes five articles a day to a blog nobody reads, "
    "then calls the zero clicks organic growth in progress."
)

EXPECTED_SHA256 = (
    "17ff06cbc25f058bddc2e54312896c8d222cfcfcf30a5dffd7458e1a6a3f658a"
)
EXPECTED_CHARS = 117


def check_gate(text):
    """Mirror the house gate: 1-200 characters, not only whitespace."""
    if not text.strip():
        raise SystemExit("roast is empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"roast is {len(text)} characters, outside the 1-200 gate"
        )


def write_entry(text):
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def read_back(path):
    """Read the file back and prove it holds exactly the intended bytes."""
    with open(path, "rb") as handle:
        raw = handle.read()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"entry.txt sha256 {digest} != expected {EXPECTED_SHA256}"
        )
    text = raw.decode("utf-8")
    if len(text) != EXPECTED_CHARS:
        raise SystemExit(
            f"entry.txt is {len(text)} chars, expected {EXPECTED_CHARS}"
        )
    return digest, len(text)


def main():
    text = ROAST.strip()
    check_gate(text)
    path = write_entry(text)
    digest, chars = read_back(path)
    print(f"wrote {path}: {chars} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
