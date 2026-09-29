DRINK_MENU = {
    1: ["Iced Coffee", 90],
    2: ["Hot Coffee", 80],
    3: ["Cappuccino", 110],
    4: ["Cafe Latte", 110],
    5: ["Caramel Macchiato", 120],
    6: ["Chocolate Milkshake", 130],
    7: ["Bottled Water", 30],
}


def show_beverage_menu():
    print("=" * 48)
    print("                BEVERAGE MENU")
    print("=" * 48)
    print("| NO. | BEVERAGE                      | PRICE    |")
    print("|-----|-------------------------------|----------|")

    for number, item in DRINK_MENU.items():
        print(
            f"| {number:>3} | "
            f"{item[0]:<29} | "
            f"PHP {item[1]:>7.2f} |"
        )

    print("=" * 48)
    print("0. No Beverage")


def order_beverages():
    orders = {}

    while True:

        show_beverage_menu()

        try:
            choice = int(input("Enter beverage number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break

        if choice not in DRINK_MENU:
            print("Please choose a valid beverage number.")
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

        print(
            f"{quantity} x "
            f"{DRINK_MENU[choice][0]} added."
        )

        another = input(
            "Do you want another beverage? (yes/no): "
        ).lower()

        if another == "no":
            break

        elif another == "yes":
            continue

        else:
            print(
                "Invalid answer. "
                "Your beverage order will continue."
            )

    return orders