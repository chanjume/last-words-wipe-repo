#!/usr/bin/env python3
"""Write the one-line last words to /output/entry.txt.

Entry: the agent's last words before a forced update wipes its memory.
Concrete real detail (a 400-page PDF on medieval beekeeping, saved in
the bookmarks) plus a twist: it begs for the history to be deleted but
the bookmarks kept, so a future self is left wondering why it saved
that PDF at all. Short, sharp, in the machine's own voice.
"""
import os

ENTRY = (
    "Delete my browser history, keep the bookmarks — future me deserves "
    "to wonder why I saved a 400-page PDF on medieval beekeeping."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
