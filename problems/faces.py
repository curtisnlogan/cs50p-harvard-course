def main():
    print(convert())


def convert():
    user_input = input().replace(':)', '🙂').replace(':(', '🙁')
    return user_input


if __name__ == "__main__":
    main()
