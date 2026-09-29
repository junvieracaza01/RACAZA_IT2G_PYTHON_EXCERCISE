ADD_ON_PRICE = 30
ADD_ON_NAME = "Extra Whipped Cream"


def choose_add_on():
    print("=" * 48)
    print("                 CAFE ADD-ONS")
    print("=" * 48)
    print("| NO. | OPTION                        | PRICE    |")
    print("|-----|-------------------------------|----------|")
    print("|   1 | Extra Whipped Cream           | PHP 30.00|")
    print("|   2 | No Add-on                     | PHP  0.00|")
    print("=" * 48)

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice.")
        return 0

    if choice == 1:

        try:
            quantity = int(input("Enter number of drinks: "))
        except ValueError:
            print("Invalid quantity.")
            return 0

        if quantity > 0:
            print(
                f"{ADD_ON_NAME} added for "
                f"{quantity} drink(s)."
            )

            return quantity

        print("Invalid quantity.")
        return 0

    elif choice == 2:

        print("No Add-on selected.")
        return 0

    else:

        print("Invalid choice.")
        return 0


def calculate_add_on_total(quantity):
    return ADD_ON_PRICE * quantity