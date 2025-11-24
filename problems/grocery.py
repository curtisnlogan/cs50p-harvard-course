"""
pseudocode
"""


def main():
    user_grocery_list = {}

    def grocery_list():
        while True:
            try:
                user_item = input("").upper()
            except EOFError:
                final_list = sorted(user_grocery_list)
                for item in final_list:
                    print(f'{user_grocery_list.get(item)} {item}')
                break
            if user_item in user_grocery_list:
                user_grocery_list[user_item] += 1
            else:
                user_grocery_list[user_item] = 1
    grocery_list()


if __name__ == "__main__":
    main()
