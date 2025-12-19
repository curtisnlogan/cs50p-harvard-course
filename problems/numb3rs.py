import re


def main():
    # defensively strip whitespace from input
    print(validate(input("IPv4 Address: ").strip()))


def validate(ipv4: str):
    # changed name from 'ip' to 'ipv4' for clarity
    # re.fullmatch instead of re.search as looking for a single full match
    octet = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    if match := re.fullmatch(
        rf"{octet}\.{octet}\.{octet}\.{octet}",
        ipv4,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
