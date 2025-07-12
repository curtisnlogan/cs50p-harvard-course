def main():
    while True:  # infinite loop allows the user to use the convert
        # function as many times as they like
        camel_case_var = input("camelCase: ")
        print(f"snake_case: {camel_to_snake(camel_case_var)}")
        break


def camel_to_snake(var):
    new_var = ""  # i wasnt building a new string originally
    # so i was just returning the original variable that was passed
    # as an argument into the function
    for letter in var:
        if letter.isupper():
            # overlooked
            # the simple ability to + the original letter onto
            # the .replace using letter.lower()
            new_var += letter.replace(letter, "_") + letter.lower()
        else:
            new_var += letter
    return new_var  # neccessary to access the variable out of


# the function scope


if __name__ == "__main__":
    main()
