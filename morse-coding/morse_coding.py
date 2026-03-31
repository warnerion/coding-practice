from __future__ import annotations

inputs = (
    "... . -... .- ... - .. .- -.  -- ..- -. --- --..  .---- ----. ----. ...--",
    "-.-. --- -.. .  .. -.  .--. -.-- - .... --- -.",
)

morse_dictionary = (
    ("E", "T"),
    (
        ("I", "A"),
        (
            ("S", "U"),
            (
                ("H", "V"),
                (("5", "4"), (), ()),
                (("", "3"), (), ()),
            ),
            (
                ("F", ""),
                (("", ""), (), ()),
                (("", "2"), (), ()),
            ),
        ),
        (
            ("R", "W"),
            (("L", ""), (), ()),
            (
                ("P", "J"),
                (("", ""), (), ()),
                (("", "1"), (), ()),
            ),
        ),
    ),
    (
        ("N", "M"),
        (
            ("D", "K"),
            (
                ("B", "X"),
                (("6", ""), (), ()),
                (("", ""), (), ()),
            ),
            (
                ("C", "Y"),
                (("", ""), (), ()),
                (("", ""), (), ()),
            ),
        ),
        (
            ("G", "O"),
            (
                ("Z", "Q"),
                (("7", ""), (), ()),
                (("", ""), (), ()),
            ),
            (
                ("", ""),
                (("8", ""), (), ()),
                (("9", "0"), (), ()),
            ),
        ),
    ),
)

tree = list(morse_dictionary)


def interpret_signal(signal: str) -> str:
    """
    Decode one Morse token using the tuple-based Morse tree.

    Examples:
        "." -> "E"
        "..." -> "S"
        ".----" -> "1"
    """
    current_tree = tree
    out_char = ""

    # TODO:
    # 1. If signal == "", return " " to represent a word boundary.
    # 2. Loop through each sign in signal.
    # 3. If sign == ".":
    #       - update out_char using current_tree[0][0]
    #       - move current_tree to current_tree[1]
    # 4. If sign == "-":
    #       - update out_char using current_tree[0][1]
    #       - move current_tree to current_tree[2]
    # 5. Return out_char.

    raise NotImplementedError


def interpret_message(message: str) -> str:
    """
    Decode a full Morse message.

    Rules:
    - single space separates characters
    - double space separates words
    """
    out_text = ""

    # TODO:
    # 1. Split message by " " into Morse tokens.
    # 2. Decode each token with interpret_signal.
    # 3. Append each decoded result into out_text.
    # 4. Return out_text.

    raise NotImplementedError


def run_examples() -> None:
    for message in inputs:
        print(message.split(" "))
        try:
            print(interpret_message(message))
        except Exception:
            print("Invalid Input")


if __name__ == "__main__":
    run_examples()