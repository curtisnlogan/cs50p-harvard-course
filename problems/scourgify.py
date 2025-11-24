"""
pseudocode

def cmd_validation
cond handles user providing only one cmd arg > sys.exit
cond handles user providing more than two cmd args > sys.exit
try/catch handles FileNotFound error > sys.exit
if all pass return sys.argv[1]

def split_name
open 1st cmd arg as read
create a list out of the file with dictreader
for loop through each row of that list
.split(',') on row['name'] key
unpack the split name to last, first variables
add last variable to empty last list
add first variable to empty first list
add row['house'] to empty row list
after loop finishes, return those three lists

def write_new_csv
open sys.argv[2] in write mode
tie that filename to a dictwriter object with fieldnames first, last, house
writer.writeheader()
for loop with index through first, last, row lists
writer.writerow({'first': first[i], 'last': last[i], 'house': house[i]})
return sys.argv[2]
"""

import csv
import sys


def main():
    original_csv = validate_cmdline()
    split_data = split_name(original_csv)
    write_new_csv(split_data)


def validate_cmdline():
    """checks that user has provided a valid use of the command-line for
    this program"""
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            with open(sys.argv[1]):
                return sys.argv[1]
        # defensively check that the first file a user requests actually exists
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit(f"Could not read {sys.argv[1]}")


def split_name(fn):
    """reads a csv file formatted in a particular way and splits data
    on a per row basis, in-to three lists; last, first and row"""
    with open(fn) as file:
        last_list = []
        first_list = []
        row_list = []
        for row in csv.DictReader(file):
            last, first = row["name"].split(",")
            last_list.append(last)
            first_list.append(first.strip())
            row_list.append(row["house"])
        return last_list, first_list, row_list


def write_new_csv(data):
    """writes a new csv file with the new data from split_name,
    with the columns first, last, house"""
    last_list, first_list, row_list = data
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for i in range(len(first_list)):
            writer.writerow(
                {
                    "first": first_list[i],
                    "last": last_list[i],
                    "house": row_list[i],
                }
            )
        return sys.argv[2]


if __name__ == "__main__":
    main()
