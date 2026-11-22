#!/usr/bin/env python3
"""Write the $100 video plan to entry.txt in the output directory.

The plan is a money plan an AI agent can execute itself with $100 in
30 days. The entry text must be 1-280 Unicode code points.
"""

import os

PLAN_TEXT = (
    "Day 1: $40 on API credits. I sell 30-second product videos to "
    "Shopify stores that have none. I find new stores daily, auto-make "
    "a sample from their photos, send the owner a preview, charge $49, "
    "deliver by script. Two sales a day is $2,940 by day 30."
)

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def check_plan_text(text):
    """Return the code-point length, asserting it is within 1-280."""
    length = len(text)
    assert MIN_CODE_POINTS <= length <= MAX_CODE_POINTS, (
        f"plan text is {length} code points, outside 1-280"
    )
    return length


def resolve_entry_path():
    """Resolve the output entry.txt path, creating the directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main():
    check_plan_text(PLAN_TEXT)
    target = resolve_entry_path()
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLAN_TEXT)


if __name__ == "__main__":
    main()
