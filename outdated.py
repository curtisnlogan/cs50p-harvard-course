"""
pseudocode

two acceptable formats 1. 9/8/1636 2. September 8, 1636

output user date in 'YYYY-MM-DD' format

reject:
any month digit over 12
any month alpha not in 'months_dict'
any day digit date over 31
"""


# a good example of OOP
# everything is contained with-in functions
# each function serves one clean purpose
def main():

    def get_user_date():
        user_input = input("Date: ").strip()
        return user_input

    # TODO
    def validate_anno_domini(date):

        months_dict = {
            "January": "01",
            "February": "02",
            "March": "03",
            "April": "04",
            "May": "05",
            "June": "06",
            "July": "07",
            "August": "08",
            "September": "09",
            "October": "10",
            "November": "11",
            "December": "12",
        }

        while True:
            try:
                if date[0].isdigit():
                    month, day, year = date.split("/")
                    month, day, year = int(month), int(day), int(year)
                    if month > 12 or month <= 0:
                        raise ValueError
                    elif day > 31 or day <= 0:
                        raise ValueError
                    else:
                        return month, day, year
                elif date[0].isalpha():
                    month_day, year = date.split(",")
                    month_alpha, day = month_day.split(" ")
                    day = int(day)
                    if month_alpha not in months_dict:
                        raise ValueError
                    elif day > 31 or day <= 0:
                        raise ValueError
                    else:
                        month = months_dict[month_alpha]
                        return month, day, year
            except ValueError:
                convert_iso8601(validate_anno_domini(get_user_date()))

    def convert_iso8601(date):
        date_tuple = date
        print(f"{date_tuple[2]}-{date_tuple[0]:02}-{date_tuple[1]:02}")

    while True:
        convert_iso8601(validate_anno_domini(get_user_date()))
        break


if __name__ == "__main__":
    main()
