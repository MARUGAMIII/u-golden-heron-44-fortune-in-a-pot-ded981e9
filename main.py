"""Fortune in a Pot entry.

Writes a single-line fortune for a houseplant to /output/entry.txt.
The text must be plain ASCII, one line, 1-120 characters, kind and
funny, with the cadence of a prediction about the plant's own future.
"""

FORTUNE = "This week the sun will linger on your leaves a little longer, and the fern beside you will ask for your secret."


def main():
    text = FORTUNE.strip()
    # Gate self-check: mirror the sealed scorer (1-120 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
