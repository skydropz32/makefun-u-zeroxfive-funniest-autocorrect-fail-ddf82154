"""Funniest Autocorrect Fail: one line, under 200 characters.

A text to Dad where autocorrect swaps "corn" for "porn" — the tacos
make the intended word obvious, and the wrong word lands the joke.
"""

LINE = "Dad, can you pick up some porn on your way home? We're having tacos tonight."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-199 characters,
    # not only white space, and a single line.
    if not (1 <= len(LINE) <= 199):
        raise ValueError("entry must be 1-199 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
