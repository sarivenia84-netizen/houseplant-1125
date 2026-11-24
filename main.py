#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one funny out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. The gate wants 1 to 120 characters, not only
white space.
"""
import os

ENTRY = ("Out of office: grew two leaves for you to ignore. "
         "Allow two weeks for me to notice your complaint.")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
