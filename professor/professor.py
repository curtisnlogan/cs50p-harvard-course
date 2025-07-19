"""
pseudocode
"""

import random


def main():
    maths_quiz(generate_integers(get_level(), 10))


def get_level():
    """
    Prompt the user to enter a difficulty level (1, 2, or 3).

    Continuously prompts the user until a valid integer
    between 1 and 3 (inclusive) is entered.
    Returns:
        int: The selected difficulty level (1, 2, or 3).
    """
    # infinite loop for re-prompting
    while True:
        # catching those pesky user input errors again
        try:
            level = int(input("Level: "))
        except ValueError:
            # forces the loop to restart, if not variable unassigned error
            # will occur on next line with 'level'
            continue
        if level < 1:
            pass
        elif level > 3:
            pass
        else:
            return level


# initially i was going to write a large amount of the program here
# remember functions asides from main() are suppose to do one thing really well
# note in the params how i documented the expected input type
def generate_integers(level=int, n=int):
    """
    Generate a list of tuples containing pairs of random non-negative integers
    based on the specified difficulty level.

    Args:
        level (int): The difficulty level indicating
        the number of digits for each integer.
            - If level == 1: returns pairs of integers in the range [0, 9].
            - If level == 2: returns pairs of integers in the range [10, 99].
            - Otherwise: returns pairs of integers in the range [100, 999].
        n (int): The number of pairs to generate.

    Returns:
        list of tuple: A list containing n tuples, each with
        two randomly generated integers of the specified digit length.
    """
    if level == 1:
        x_y_pairs = []
        # if one does not care about the variable use _
        for _ in range(n):
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
            # passing more than one arg will append as nested list
            x_y_pairs.append((x, y))
        return x_y_pairs
    elif level == 2:
        x_y_pairs = []
        for _ in range(n):
            x = random.randrange(10, 100)
            y = random.randrange(10, 100)
            x_y_pairs.append((x, y))
        return x_y_pairs
    else:
        x_y_pairs = []
        for _ in range(n):
            x = random.randrange(100, 1000)
            y = random.randrange(100, 1000)
            x_y_pairs.append((x, y))
        return x_y_pairs


def maths_quiz(n_pairs):
    """ """
    user_score = 0
    for pair in n_pairs:
        user_attempts = 0
        while True:
            try:
                user_ans = int(input(f"{pair[0]} + {pair[1]} = "))
            except ValueError:
                continue
            if user_attempts == 3:
                print(pair[0] + pair[1])
                break
            elif user_ans != pair[0] + pair[1]:
                print("EEE")
                user_attempts += 1
                pass
            else:
                user_score += 1
                break
    print(user_score)


if __name__ == "__main__":
    main()
