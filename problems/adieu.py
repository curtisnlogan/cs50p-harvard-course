"""
pseudocode
"""

import inflect


def main():
    def adieu_adieu_list():
        inflect_inst = inflect.engine()
        user_name_list = []
        while True:
            try:
                user_name = input("Name: ")
                user_name_list.append(user_name)
            except EOFError:
                print(f"Adieu, adieu, to {inflect_inst.join(user_name_list)}")
                break

    adieu_adieu_list()


if __name__ == "__main__":
    main()
