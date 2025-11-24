# just like when planning before writing an essay
# pseudocode is a crucial element of good programming
"""
pseudocode
"""


def main():  # all code to be excuted goes here, how neat and tidy!
    coke_machine()


def coke_machine():
    AMOUNT_DUE = 50  # assuming the price will be a constant
    #  no need to have the variable be of a global scope
    while True:
        if AMOUNT_DUE == 0:
            # * 0 by negative 0 does not work
            print(f"Change Owed: {AMOUNT_DUE}")
            break
        elif AMOUNT_DUE < 0:
            # mathematical operation here that gets me the positive
            # for any negative number
            print(f"Change Owed: {AMOUNT_DUE * -1}")
            break
        print(f"Amount Due: {AMOUNT_DUE}")
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin == 5:
            # pythonic with the '-=' more clean
            AMOUNT_DUE -= 5
        elif inserted_coin == 10:
            AMOUNT_DUE -= 10
        elif inserted_coin == 25:
            AMOUNT_DUE -= 25


if __name__ == "__main__":
    main()
