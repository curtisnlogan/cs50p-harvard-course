import datetime
import inflect
import re
import sys


def main():
    user_dob = get_dob()
    user_mins = calc_mins_since_dob(user_dob)
    print(convert_mins_to_words(user_mins))


def get_dob():
    dob_regex_pattern = r"^\d{4}-\d{2}-\d{2}$"
    user_input = input("What is your DOB in YYYY-MM-DD (must be exact)?: ")
    if match := re.search((dob_regex_pattern), user_input):
        return str(match.group(0))
    else:
        sys.exit("Invalid Date of Birth format. Please try again.")


def calc_mins_since_dob(dob: str):
    today = datetime.date.today()
    str_today = str(today)
    dt_today = datetime.datetime.strptime(str_today, "%Y-%m-%d")
    dt_dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
    time_diff = dt_today - dt_dob
    return time_diff.days * 1440


def convert_mins_to_words(minutes: int):
    p = inflect.engine()
    mins_as_words = p.number_to_words(minutes) + " minutes"
    mins_as_words = mins_as_words.replace(" and ", " ")
    return mins_as_words.capitalize()


if __name__ == "__main__":
    main()
