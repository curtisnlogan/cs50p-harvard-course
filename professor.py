"""
pseudocode
"""

import random


def main():
    maths_quiz(generate_integer(get_level()))


def get_level():
    """
    Prompt the user to enter a difficulty level (1, 2, or 3).

    Continuously prompts the user until a valid integer
    between 1 and 3 (inclusive) is entered.
    Returns:
        int: The selected difficulty level (1, 2, or 3).
    """
    # "infinite" loop for re-prompting
    while True:
        # catching those pesky user input errors once again
        try:
            level = int(input("Level: "))
        # except should be here and not further down in the function
        # as the above line of code is the only thing i want to try here
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
# i originally did level=int for a para, thinking that it was readability
# showing hey this para should have an int, instead it set the default value
# to 'int' literally, which is not what i wanted!
def generate_integer(level=1):
    """
    Generate a list containing random non-negative integers
    based on the specified difficulty level.

    Args:
        level (int): The difficulty level indicating
        the number of digits for each integer.
            - If level == 1: returns pairs of integers in the range [0, 9].
            - If level == 2: returns pairs of integers in the range [10, 99].
            - Otherwise: returns pairs of integers in the range [100, 999].

    Returns:
        list: A list containing integers, randomly generated, based on the
        level arg provided
    """
    if level == 1:
        random_integers = []
        # if one does not care about the variable use _
        for _ in range(20):
            # randrange is exclusive at the end point
            n = random.randrange(0, 10)
            random_integers.append(n)
        return random_integers
    elif level == 2:
        random_integers = []
        for _ in range(20):
            n = random.randrange(10, 100)
            random_integers.append(n)
        return random_integers
    else:
        random_integers = []
        for _ in range(20):
            n = random.randrange(100, 1000)
            random_integers.append(n)
        return random_integers


def maths_quiz(rand_integers):
    """
    Conducts a simple math quiz using pairs of integers from the provided list.

    For each consecutive pair of integers in `rand_integers`, the user is
    prompted to solve an addition problem.
    The user has up to three attempts to provide the
    correct answer for each question. If the user fails to answer
    correctly within three attempts, the correct answer is displayed.
    The user's score is incremented for each
    correct answer and displayed at the end of the quiz.

    Args:
        rand_integers (list of int): A list of integers,
        where each consecutive pair forms an addition question.

    Returns:
        None
    """
    # if in infinite loop it will reset on every rerun
    # should not be in for loop either as its not tied to anything per question
    user_score = 0
    # len func is inclusive at end point, step in range key here to grab pairs!
    for n in range(0, len(rand_integers), 2):
        user_attempts = 0
        # interesting use of slicing, remember slicing is exclusive
        pair = rand_integers[n: n + 2]
        while True:
            # im checking if the user is out of attempts before asking them
            # again, made mistake of asking them for ans when out of inputs
            # by putting this conditional block after the input request
            if user_attempts == 3:
                print(f"{pair[0] + pair[1]}")  # Show correct answer
                break
            try:
                user_ans = int(input(f"{pair[0]} + {pair[1]} = "))
            except ValueError:
                # If input is not an integer, prompt again without penalty
                continue
            if user_ans != (pair[0] + pair[1]):
                print("EEE")  # Indicate incorrect answer
                user_attempts += 1
                pass
            else:
                user_score += 1  # Increment score for correct answer
                break
    print(f"Score: {user_score}")  # Display final score


if __name__ == "__main__":
    # Entry point for the script; starts the quiz
    main()
