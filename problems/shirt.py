"""
pseudocode

* func validate proper command-line use (reuse from prior question)
The program should exit via sys.exit if
1. if the user does not specify exactly two command-line arguments
2. if the input’s and output’s names do not end in .jpg, .jpeg, or .png,
case-insensitively (.lower() then check)
3. if the input’s name does not have the same extension as the output’s name
(use == to check for equality of input/output)
4. if the specified input arg does not exist (FileNotFoundError)

* func open input arg with Image.open("")

resize and crop input with ImageOps.fit(resize, paste.size)
* func paste overlay image onto input with paste() using default values for
method, bleed, centering
save the result with .save()
"""

import os
import sys
from PIL import Image, ImageOps


def main():
    input_fn = validate_cmdline()
    input_obj = resize_image(input_fn)
    add_to_image(input_obj)


def validate_cmdline():
    """checks that user has provided a valid use of the command-line for
    this program"""
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # TODO
    elif (
        sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) is not True
        or sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")) is not True
    ):
        sys.exit("Invalid input or output")
    _, ext_1 = os.path.splitext(sys.argv[1])
    _, ext_2 = os.path.splitext(sys.argv[2])
    if ext_1 != ext_2:
        sys.exit("Input and output have different extensions")
    else:
        try:
            with open(sys.argv[1]):
                return sys.argv[1]
        # defensively check that input file a user requests actually exists
        except FileNotFoundError:
            sys.exit("Input does not exist")


def resize_image(fn):
    """accepts an image that needs to be resized and does so using the 'fit'
    func from ImageOps in PIL"""
    with Image.open(fn) as resize, Image.open("shirt.png") as base:
        resized_img = ImageOps.fit(resize, base.size)
        return resized_img


def add_to_image(sized_img):
    with Image.open("shirt.png") as paste:
        sized_img.paste(paste, mask=paste)
    sized_img.save(sys.argv[2])
    sized_img.close()


if __name__ == "__main__":
    main()
