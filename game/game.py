"""
pseudocode
"""

import random


# all code to be executed is contained within this single function
def main():
    def guessing_game():
        while True:
            # error catching, incorrect user input is a common one
            try:
                user_level = int(input("Level: "))
            # catching input that cannot be converted to an integer
            except ValueError:
                # force loop restart otherwise program will continue
                # and the user_level variable will throw error as it won't
                # exist!
                continue
            if user_level < 1:
                # this will re-prompt as pass means do nothing
                pass
            # code is now okay so lets break out of this infinite loop here
            else:
                break
            # random.randrange was problematic if the user inputted a level
            # of 1, as there is of-course no range between 1 and 1
        random_n = random.randint(1, user_level)
        while True:
            try:
                user_guess = int(input("Guess: "))
            except ValueError:
                continue
            if user_guess < 1:
                # including pass makes it more readable, implies the loop
                # will restart again
                pass
            elif user_guess < random_n:
                print("Too small!")
                pass
            elif user_guess > random_n:
                print("Too large!")
                pass
            else:
                print("Just right!")
                break

    guessing_game()


if __name__ == "__main__":
    main()
