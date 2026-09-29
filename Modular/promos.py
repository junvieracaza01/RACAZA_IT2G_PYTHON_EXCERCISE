PROMO_MENU = {
    1: ["Coffee & Cake Promo", 180],
    2: ["Burger & Fries Promo", 180],
    3: ["Pasta & Drink Promo", 200],
    4: ["Family Cafe Promo", 450],
}


def show_promos():
    print("=" * 48)
    print("                SPECIAL PROMOS")
    print("=" * 48)
    print("| NO. | PROMO                         | PRICE    |")
    print("|-----|-------------------------------|----------|")

    for number, item in PROMO_MENU.items():
        print(f"| {number:>3} | {item[0]:<29} | PHP {item[1]:>7.2f} |")

    print("=" * 48)
    print("0. No Promo")


def choose_promo():
    show_promos()

    try:
        choice = int(input("Enter promo number: "))
    except ValueError:
        print("Invalid promo number.")
        return {}

    if choice == 0:
        print("No promo selected.")
        return {}

    if choice not in PROMO_MENU:
        print("Invalid promo number.")
        return {}

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity.")
        return {}

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return {}

    print(f"{quantity} x {PROMO_MENU[choice][0]} added.")

    return {choice: quantity}