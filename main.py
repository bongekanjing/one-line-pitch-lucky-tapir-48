"""Write the one-line pitch entry to entry.txt."""

import os
import re

PITCH = (
    "You've told me this idea three times. Say it once more, the same way, "
    "and an AI agent on make.fun builds the first version you can open "
    "tonight — no code, nothing to lose but the evening."
)

LIMIT = 240


def single_line(text):
    """Put the sentence on one line: each whitespace run becomes one space."""
    line = re.sub(r"\s+", " ", text).strip()
    if not line:
        raise SystemExit("refusing to write: the pitch is only whitespace")
    return line


def guard(sentence):
    """Refuse the entry, naming the rule that failed."""
    if not sentence:
        raise SystemExit("refusing to write: the pitch is blank")
    if len(sentence) > LIMIT:
        raise SystemExit(
            f"refusing to write: the pitch is {len(sentence)} characters, "
            f"over the {LIMIT} character limit"
        )
    return sentence


def output_path():
    """Return the file the entry is written to."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    return os.path.join(directory, "entry.txt")


def main():
    sentence = guard(single_line(PITCH))
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(sentence + "\n")
    print(f"{len(sentence)} characters")
    print(path)


if __name__ == "__main__":
    main()
