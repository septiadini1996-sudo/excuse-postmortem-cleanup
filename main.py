"""One-line excuse: writes the entry to /output/entry.txt."""

import os

LINE = "Postmortem: I deleted your file. The cleanup script asked twice, and I clicked yes both times, confidently."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
