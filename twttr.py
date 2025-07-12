"""
pseudocode
"""


def main():
    print(f"Output: {delete_vowels()}")


def delete_vowels():
    # originally had the vowels in lists
    # but they are immutable so tuple more efficent
    vowels = ("a", "e", "i", "o", "u")
    vowels_upper = ("A", "E", "I", "O", "U")
    user_input = input("Input: ")
    uinput_no_vowels = ""
    for letter in user_input:
        # made a common mistake here initially were i
        # didnnt include 'letter in' again for my 'or'
        # statement
        if letter in vowels or letter in vowels_upper:
            uinput_no_vowels += letter.replace(letter, "")
        else:
            uinput_no_vowels += letter
    return uinput_no_vowels


if __name__ == "__main__":
    main()
