"""
pseudocode
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


"""
function: 'is_valid(s)'
"""


def is_valid(s):
    alphabet_upper = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    single_digits = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    user_plate = ""

    for alnum in s:
        user_plate += alnum

    # all vanity plates must start with at least two letters.
    for alnum in user_plate[0:2]:
        if alnum in single_digits:
            return False

    # vanity plates may contain a maximum of 6 characters
    # and a minimum of 2 characters.
    if len(user_plate) < 2:
        return False
    if len(user_plate) > 6:
        return False

    # numbers cannot be used in the middle of a plate;
    # they must come at the end.
    # for example, AAA222 would be an acceptable,
    # AAA22A would not be acceptable.
    for alnum in user_plate:
        if alnum.isdigit():
            if user_plate[-1] in alphabet_upper:
                return False
            if user_plate[-2] in alphabet_upper:
                return False

    # the first number used cannot be a 0.
    for alnum in user_plate:
        if alnum == "0":
            return False
        elif alnum in single_digits:
            break

    # no periods, spaces, or punctuation marks are allowed.
    for alnum in user_plate:
        if alnum not in alphabet_upper and alnum not in single_digits:
            return False

    # if all return Falses failed then must be True
    return True


if __name__ == "__main__":
    main()
