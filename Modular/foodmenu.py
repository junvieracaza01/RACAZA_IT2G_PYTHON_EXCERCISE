FOOD_MENU = {
    1: ["Cheeseburger", 120],
    2: ["Chicken Sandwich", 110],
    3: ["Club Sandwich", 130],
    4: ["Tuna Sandwich", 100],
    5: ["French Fries", 70],
    6: ["Nachos", 90],
    7: ["Carbonara", 150],
    8: ["Spaghetti", 140],
    9: ["Chicken Pasta", 160],
    10: ["Lasagna", 170],
    11: ["Pancakes", 100],
    12: ["Waffles", 110],
    13: ["Chocolate Cake", 120],
    14: ["Cheesecake", 130],
    15: ["Donut", 60],
    16: ["Cookies", 50],
}


def show_food_menu():
    print("=" * 48)
    print("                  FOOD MENU")
    print("=" * 48)
    print("| NO. | FOOD                          | PRICE    |")
    print("|-----|-------------------------------|----------|")

    for number, item in FOOD_MENU.items():
        print(f"| {number:>3} | {item[0]:<29} | PHP {item[1]:>7.2f} |")

    print("=" * 48)


def order_food():
    orders = {}

    while True:
        show_food_menu()

        try:
            choice = int(input("Enter food number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice not in FOOD_MENU:
            print("Please choose a valid food number.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        orders[choice] = orders.get(choice, 0) + quantity

        print(f"{quantity} x {FOOD_MENU[choice][0]} added.")

        another = input(
            "Do you want to order another food? (yes/no): "
        ).lower()

        if another == "no":
            break

        if another != "yes":
            print("Invalid answer. Your food order will continue.")

    return orders