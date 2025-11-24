""" """

import csv
import sys
from tabulate import tabulate


def main():
    fn = validate_cmdline()
    dicts = csv_to_dicts(fn)
    print(tabulate(dicts, headers="keys", tablefmt="grid"))


def validate_cmdline():
    """checks that user has provided a valid use of the command-line"""
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]):
                return sys.argv[1]
        # defensively check that the file a user requests actually exists
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


def csv_to_dicts(fn):
    """takes a csv file, reads it as dict and saves the rows as a list
    of dicts"""
    with open(fn) as file:
        # creates the dict reader object
        data = []
        for row in csv.DictReader(file):
            data.append(row)
        return data


if __name__ == "__main__":
    main()
