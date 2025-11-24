"""
grab file name entered by user with sys.argv[1]

defensive programming:
handle not one command-line arg then sys.exit
handle file not ending in .py then sys.exit

open the above file
handle file not existing with 'FileNotFoundError' then sys.exit

for loop through the file run strip() on all lines first

for loop: if starts with # (startswith method) ignore or a line which contains
only whitespace ("") ignore, otherwise add 1 to a counter variable

6. return that counter variable after loop ends

7. print the number of lines of code(counter) in that file
"""

# to access sys.argv
import sys


def main():
    file = validate_cmd()
    print(count_total_lines(file))


def validate_cmd():
    """reads a python file and then removes all whitespace on each line"""
    # check user has used the command-line in expected way
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py"):
        # defensively check that the file a user requests actually exists
        try:
            with open(sys.argv[1]):
                return sys.argv[1]
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")


def count_total_lines(file: str):
    """takes a python file and counts the total number of lines"""
    counter = 0
    with open(file) as doc:
        for line in doc:
            if line.strip().startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                counter += 1
        return counter


if __name__ == "__main__":
    main()
