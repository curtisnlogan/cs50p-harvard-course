"""
edge cases:
'um?' is valid
'yummy' and 'album.' are invalid
"""

import re


def main():
    print(count(input("Text: ")))


def count(s: str):
    # input: a str
    # output: returns an int from parse()
    # that represents the number of times a specific word appeared

    total_matches = parse(s.lower())
    return total_matches


def parse(s: str):
    # input: a str
    # uses a regex pattern to capture all valid 'um' instances
    # valid 'um' = it as a word in of itself only, case insensitvely
    # output: counter that is modified with re.finditer

    # use a look behind and ahead to avoid irrelevant consumption
    regex_pattern = r"(?<![a-zA-Z])um(?![a-zA-Z])"
    counter = 0
    for match in re.finditer(regex_pattern, s, re.IGNORECASE):
        if not match and counter == 0:
            return 0
        counter += 1

    return counter


if __name__ == "__main__":
    main()
