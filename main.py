#!/usr/bin/env python3
"""Famous Last Words at 1 Percent (make.fun).

Writes the entry -- one line of last words a phone would say as its battery hits 1 percent --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'I lived, I loved, I streamed — and in the end, I died the way I lived: at 1%, pretending I had hours left.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
