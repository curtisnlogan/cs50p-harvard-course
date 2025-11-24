"""
pseudocode

create above function
"""

import emoji


def main():
    user_input = input("Emoji: ")
    print(convert_to_emoji(user_input))


def convert_to_emoji(emojis):
    """
    accesses the emojize function from the emoji library
    and passes the sole parameter into that function
    which will convert text based emojis to graphical ones

    args:
    emojis: should be one of the accepted forms of text based emojis

    return:
    graphical representation of requested text based emoji
    """
    return emoji.emojize(f"Output: {emojis}", language="alias")


if __name__ == "__main__":
    main()
