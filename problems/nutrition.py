"""
pseudocode
"""


def main():
    user_fruit = input("Type in a fruit: ").title()
    fruit_calories(user_fruit)


fda_fruit = {
    "Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Grapes": "90",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Lime": "20",
    "Nectarine": "60",
    "Orange": "80",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plums": "70",
    "Strawberries": "50",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80",
}


def fruit_calories(fruit):
    if fruit in fda_fruit:
        print(f"Calories: {fda_fruit[fruit]}")
    else:
        print("")


if __name__ == "__main__":
    main()
