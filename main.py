import os

HANDLE = "anata-dare"


def build_entry(handle):
    """Return the entry text: one word, the entrant's own handle, nothing else."""
    word = handle.strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("handle must be a single word of 1-30 characters")
    return word


def main():
    output_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(build_entry(HANDLE))


if __name__ == "__main__":
    main()
