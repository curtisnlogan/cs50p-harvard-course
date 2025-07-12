"""
pseudocode
"""


def main():
    # infinite loop allows for repromoting user easily
    while True:
        user_fraction = input("Fraction: ")
        if "/" not in user_fraction:
            main()
        else:
            # 'split' can be used to set a seperator
            # from which the a str can be split
            # the result can then be passed
            # in-to multiple variables at once
            n_1, n_2 = user_fraction.split("/")
        # one should handle errors in python specifically as below
        # not vaguely with broad 'except Exceptions'
        try:
            if n_2 == "0":
                raise ZeroDivisionError("You cannot divide by 0.")
            elif n_1 == n_1.isalpha() or n_2.isalpha():
                raise ValueError("Numeric characters only.")
            # a way to look for if x 'in' y
            # 'or' means if either is true then step-in
            elif "." in n_1 or "." in n_2:
                raise ValueError("Integers only.")
        # if you raise an exception as above, its good practice
        # to handle it as below through 'except x as y:'
        # brackets can be used to deal with multiple raises at once
        except (ZeroDivisionError, ValueError) as e:
            # will print out the text i decided upon when i raised the errors
            print(f"Error: {e}")
            user_restart = input("Do you want to try again? y/n: ").lower().strip()
            if user_restart == "y":
                main()
            else:
                break
        # can now be confident to convert into int due to no errs
        n_1 = int(n_1)
        n_2 = int(n_2)
        # needed to check this error here as i need them to be integers
        # to do the greater or lesser comparisons with '>'
        try:
            if n_1 > n_2:
                raise ValueError("The first number cannot be greater than the second.")
        except ValueError as e:
            print(f"Error: {e}")
            user_restart = input("Do you want to try again? y/n: ").lower().strip()
            if user_restart == "y":
                main()
            else:
                break
        # calling my function with user input as args
        fuel_tank = frac_to_perc(n_1, n_2)
        if fuel_tank > 1 and fuel_tank < 99:
            print(f"{fuel_tank}%")
            break
        elif fuel_tank <= 1:
            print("E")
            break
        else:
            print("F")
            break


def frac_to_perc(n_1, n_2):
    calc = n_1 / n_2
    calc_2 = round(calc * 100)
    return calc_2


if __name__ == "__main__":
    main()
