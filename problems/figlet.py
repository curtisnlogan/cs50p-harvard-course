"""
pseudocode
"""

# this section deals with external libraries
# importing for command-line arguments primarily
import sys

# stops one from using the word Figlet in ones own variables etc.
# which is okay
from pyfiglet import Figlet

# required for the random feature of this converter function
import random

# list of all avaiable fonts in the pyfiglet module required
# for the random font feature
pyfiglet_fonts = [
    "3-d",
    "3x5",
    "acrobatic",
    "alligator",
    "alligator2",
    "alphabet",
    "avatar",
    "banner",
    "banner3-D",
    "banner3",
    "banner4",
    "barbwire",
    "basic",
    "bell",
    "big",
    "bigchief",
    "binary",
    "block",
    "bubble",
    "bulbhead",
    "calgphy2",
    "caligraphy",
    "catwalk",
    "chunky",
    "coinstak",
    "colossal",
    "computer",
    "contessa",
    "contrast",
    "cosmic",
    "cosmike",
    "cricket",
    "cursive",
    "cyberlarge",
    "cybermedium",
    "cybersmall",
    "diamond",
    "digital",
    "doh",
    "doom",
    "dotmatrix",
    "drpepper",
    "eftichess",
    "eftifont",
    "eftipiti",
    "eftirobot",
    "eftitalic",
    "eftiwall",
    "eftiwater",
    "epic",
    "fender",
    "fourtops",
    "fuzzy",
    "goofy",
    "gothic",
    "graffiti",
    "hollywood",
    "invita",
    "isometric1",
    "isometric2",
    "isometric3",
    "isometric4",
    "italic",
    "ivrit",
    "jazmine",
    "jerusalem",
    "katakana",
    "kban",
    "larry3d",
    "lcd",
    "lean",
    "letters",
    "linux",
    "lockergnome",
    "madrid",
    "marquee",
    "maxfour",
    "mike",
    "mini",
    "mirror",
    "mnemonic",
    "morse",
    "moscow",
    "nancyj-fancy",
    "nancyj-underlined",
    "nancyj",
    "nipples",
    "ntgreek",
    "o8",
    "ogre",
    "pawp",
    "peaks",
    "pebbles",
    "pepper",
    "poison",
    "puffy",
    "pyramid",
    "rectangles",
    "relief",
    "relief2",
    "rev",
    "roman",
    "rot13",
    "rounded",
    "rowancap",
    "rozzo",
    "runic",
    "runyc",
    "sblood",
    "script",
    "serifcap",
    "shadow",
    "short",
    "slant",
    "slide",
    "slscript",
    "small",
    "smisome1",
    "smkeyboard",
    "smscript",
    "smshadow",
    "smslant",
    "smtengwar",
    "speed",
    "stampatello",
    "standard",
    "starwars",
    "stellar",
    "stop",
    "straight",
    "tanja",
    "tengwar",
    "term",
    "thick",
    "thin",
    "threepoint",
    "ticks",
    "ticksslant",
    "tinker-toy",
    "tombstone",
    "trek",
    "tsalagi",
    "twopoint",
    "univers",
    "usaflag",
    "wavy",
    "weird",
]


# ALL code to be executed belong in here
def main():
    # well named function
    def text_to_figlet():
        """
        This function takes some user text and returns it in the
        figlet format using an external module. It performs basic validation
        to ensure the correct two command-line arguments are provided,
        if they are.
        :params: None
        :raises general error: If the user provides the wrong two command-line
        arguments. accepting only -f or --font for the first argv and
        only a font avaiable in the pyfiglet module for the second argv
        :returns: The text formatted in the figlet style.
        :rtype: str
        """

        # this was tricky, i forgot that you could check sys.argv as a list
        # and thus use len func to see how many arguments
        # have been provided by the user
        if len(sys.argv) == 2:
            # exits program smoothly
            sys.exit(1)
        # triggers the random font feature
        elif len(sys.argv) == 1:
            # the len func counts from 1 so the -1 at the end
            # is needed when using it on a list which start from 0
            random_index = random.randint(0, len(pyfiglet_fonts) - 1)
            # this was the cause of my final debugging problem
            # i forgot that this created an instance of a class
            # assumed it was just creating a variable from some return
            # in a function call
            f = Figlet(font=pyfiglet_fonts[random_index])
            user_text = input("Enter the text to be rendered by figlet: ")
            # calling the class instance with correct font and passing in the
            # user text through varaible use
            return f.renderText(user_text)

        elif (
            # this also caused issues for me
            # i was specific enough with my conditional
            # syntax
            sys.argv[1] == "-f"
            and sys.argv[2] in pyfiglet_fonts
            or sys.argv[1] == "--font"
            and sys.argv[2] in pyfiglet_fonts
        ):
            f = Figlet(font=sys.argv[2])
            user_text = input("Enter text to be rendered by figlet: ")
            return f.renderText(user_text)
        # anything else should be rejected as described by p-set
        # hence the else use here
        else:
            sys.exit(1)

    # i only returned the text in the function so now it
    # needs to be displayed to the user
    print(text_to_figlet())


if __name__ == "__main__":
    main()
