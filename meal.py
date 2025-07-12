'''
pseudocode
1. prompt user for a time (asume that the users input
will be formatted in 24-hour time as #:## or ##:##)
2. then print if its breakfast time (7-8), lunch time (12-13)
or dinner time(18-19)
3. if its not time for any meal, output nothing at all
'''


def main():
    user_input = input('What time is it? ')
    time = convert(user_input)
    # made the below conditional structural leaner than i originally had
    # it through using 'or' instead of another 'elif'
    if time >= 7.0 and time <= 8.0:
        print('breakfast time')
    elif time >= 12.0 and time <= 13.0:
        print('lunch time')
    elif time >= 18.0 and time <= 19.0:
        print('dinner time')
    else:
        pass


def convert(time):
    # 'split' method on 'str' useful for multiple variable assignment
    hours, minutes = time.split(":")
    # had to look up the maths on this due to poor mathematical
    # skills, i didn't understand how to convert 7:30 to 7.5
    # i got 7.3 instead
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
