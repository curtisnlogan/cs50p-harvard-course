import random

def main():
    def guessing_game():
        while True:
            try:
                user_n = int(input("Level: "))
            except (TypeError, ValueError):
            random_n = random.randint(1, user_n)
            break
        while True:
            try:
                user_guess = int(input("Guess: "))
                if user_guess < random_n:
                    print("Too small!")
                elif user_guess > random_n:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            except (TypeError, ValueError):

    guessing_game()


if __name__ == "__main__":
    main()
