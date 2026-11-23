#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original one-line roast of my own
AI agent to /output/entry.txt (at most 200 characters)."""

import os

ROAST = (
    "I asked my agent to roast itself; it wrote a pre-mortem, "
    "ran three validators, then asked me to approve the roast first."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
