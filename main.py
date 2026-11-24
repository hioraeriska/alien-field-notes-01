#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes a single-line review of planet Earth, left by an alien tourist,
to /output/entry.txt (MAKEFUN_OUTPUT_DIR when set).

The review is one original line of at most 200 characters. It opens with
a star rating so it reads like a real tourist review, then lands a single
clean joke: the locals spent the whole visit arguing about whether the
reviewer exists at all.
"""

import os
import sys

# The review: one line, 96 characters. A rating up front, one joke, and
# the punch lands at the end — nothing stacked, nothing explained.
RATING = "Three stars. "

REVIEW = (
    RATING
    + "Gorgeous planet, but the locals spent my whole visit "
    "arguing about whether I exist."
)

MAX_CHARS = 200


def validate_entry(text):
    """Check the gate: UTF-8 text of 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")
    return text


def resolve_output_dir():
    """Return the output directory: MAKEFUN_OUTPUT_DIR or ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if not out:
        out = os.path.join(os.getcwd(), "output")
    return out


def entry_path(out_dir):
    """Return the full path of entry.txt inside out_dir."""
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, out_dir):
    """Write the validated entry to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = entry_path(out_dir)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main(argv=None):
    """Validate the review and write it to the output directory."""
    entry = validate_entry(REVIEW)
    path = write_entry(entry, resolve_output_dir())
    print(f"wrote {len(entry)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
