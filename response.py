from validator_collection import validators


def main():
    # handles validators from library raising errs
    try:
        if validate_email(input("Enter email: ")):
            print("Valid")
    except (validators.errors.EmptyValueError, ValueError):
        print("Invalid")


def validate_email(email: str):
    # use tested email func from validators
    # raises errs if no input or if bad, needs to be handle by caller
    return validators.email(email)


if __name__ == "__main__":
    main()
