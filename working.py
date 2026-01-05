import re
import sys


def main():
    # defensively strip() and lower() for consistency
    user_input = input("Hours: ")
    # handle any ValueErrors that are raised
    try:
        # one function calls all others required for spec conversion
        # no need to make them reuseable for this assignment
        print(convert(user_input))
    except ValueError:
        print("ValueError")
        # indicates error and aborts program
        sys.exit(1)


def convert(time_range: str):
    # orchestrator function
    # normalize input so downstream logic always sees lowercase am/pm
    time_range = time_range.strip().lower()
    # parse returns a dict of basic regex checked time parts
    parsed_time_range = parse(time_range)
    # validate uses python for advanced validation of time dict
    validated_time_dict = validate(parsed_time_range)
    # handles the conversion of the 12 to 24 hour time format
    str_conversion = conversion(validated_time_dict)
    # printable str of the final conversion
    return str_conversion


def parse(time_range: str):
    # uses a regex pattern for basic validation and to capture seperate time parts for conversion
    valid_time_pattern = (
        r"^(?P<start_hr>\d{1,2})"
        r"(?::(?P<start_min>\d{2}))?"
        r"\s{1}(?P<start_ampm>am|pm)"
        r"\s+(?:to|till)\s+(?P<end_hr>\d{1,2})"
        r"(?::(?P<end_min>\d{2}))?"
        r"\s{1}(?P<end_ampm>am|pm)$"
    )
    # re.search() allows for the naming of groups for readability
    if matches := re.search((valid_time_pattern), time_range, re.IGNORECASE):
        time_range_dict = matches.groupdict()
        # a clean readable dict of 4-6 time parts depending on input
        return time_range_dict
    else:
        # handle bad user input per spec
        raise ValueError()


def validate(time_range_dict: dict):
    # uses python itself to validate correct numerical ranges for time inputs
    # much easier than with regex!

    # a simple for loop that converts time values into ints
    # then uses comparisons to ensure valid numerical time ranges
    for key in time_range_dict.keys():
        # deals with minute values being None for subsequent .isdigit() check
        if (key == "start_min" or key == "end_min") and time_range_dict[key] is None:
            continue
        # .isdigit() ignores am/pm keys
        if time_range_dict[key].isdigit():
            # converts all digits to ints for subsequent comparison
            time_range_dict[key] = int(time_range_dict[key])
        if (key in ["start_hr", "end_hr"] and time_range_dict[key] >= 13) or (
            key in ["start_min", "end_min"] and time_range_dict[key] >= 60
        ):
            raise ValueError()
    # return validated time dict
    return time_range_dict


# TODO
def conversion(validated_time_parts: dict):
    # maintains integrity of original data through using .copy()
    converted_time = validated_time_parts.copy()

    # converts int mins that are less than 9 to the str == with the appropriate leading zero
    if validated_time_parts["start_min"] is None:
        converted_time["start_min"] = "00"
    elif validated_time_parts["start_min"] <= 9:
        converted_time["start_min"] = f"0{validated_time_parts['start_min']}"
    if validated_time_parts["end_min"] is None:
        converted_time["end_min"] = "00"
    elif validated_time_parts["end_min"] <= 9:
        converted_time["end_min"] = f"0{validated_time_parts['end_min']}"

    # handles hour conversions being 12 am or 12 pm
    if validated_time_parts["start_hr"] == 12:
        if validated_time_parts["start_ampm"] == "am":
            converted_time["start_hr"] = "00"
        # must be pm
        else:
            converted_time["start_hr"] = "12"
    if validated_time_parts["end_hr"] == 12:
        if validated_time_parts["end_ampm"] == "am":
            converted_time["end_hr"] = "00"
        else:
            converted_time["end_hr"] = "12"

    # handles 1-11 start hr conversions depending on if am or pm
    if validated_time_parts["start_hr"] <= 11:
        if validated_time_parts["start_ampm"] == "am" and validated_time_parts["start_hr"] <= 9:
            converted_time["start_hr"] = str(f"0{validated_time_parts['start_hr']}")
        elif validated_time_parts["start_ampm"] == "pm":
            converted_time["start_hr"] = str(12 + validated_time_parts["start_hr"])

    # handles 1-11 end hr conversions depending on if am or pm
    if validated_time_parts["end_hr"] <= 11:
        if validated_time_parts["end_ampm"] == "am" and validated_time_parts["end_hr"] <= 9:
            converted_time["end_hr"] = str(f"0{validated_time_parts['end_hr']}")
        elif validated_time_parts["end_ampm"] == "pm":
            converted_time["end_hr"] = str(12 + validated_time_parts["end_hr"])

    # concatenate converted dict to return a converted_time str
    conversion_output = (
        f"{converted_time['start_hr']}:{converted_time['start_min']}"
        f" to {converted_time['end_hr']}:{converted_time['end_min']}"
    )

    return conversion_output


if __name__ == "__main__":
    main()
