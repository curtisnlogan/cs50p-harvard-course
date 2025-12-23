import re


def main():
    user_input = input("Enter some HTML: ")
    validated_url = parse(user_input)
    print(validated_url)


def parse(s: str):
    if match := re.search(r"<iframe.+?src=\".*?youtube\.com/embed/(\w+)\".*", s):
        parsed_url = "https://youtu.be/" + match.group(1)
        return parsed_url
    else:
        return None


if __name__ == "__main__":
    main()
