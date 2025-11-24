"""
pseudocode
"""


def main():
    entrees = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    def order_list():
        entrees_total = 0
        while True:
            try:
                user_choice = input("Item: ").title()
            except EOFError:
                entrees_total = 0
                print("\n")
                break
            if user_choice in entrees:
                cost = entrees.get(user_choice)
                entrees_total += cost
                print(f"Total: ${entrees_total:.2f}")

    order_list()


if __name__ == "__main__":
    main()
