from promos import choose_promo
from Modular.foodmenu import order_food
from Modular.cafeaddson import choose_add_on
from Modular.beverage import order_beverages
from order import calculate_subtotal
from Modular.discount import choose_discount
from ticket import print_ticket


def main():

    print("=" * 48)
    print("                    JUN'S CAFE")
    print("=" * 48)
    print("              ENTER 1 TO ORDER")
    print("-" * 48)

    while True:

        try:
            start = int(input("Enter: "))
        except ValueError:
            print("Please enter 1 to start your order.")
            continue

        if start == 1:
            break

        print("Please enter 1 to start your order.")

    promo_orders = choose_promo()

    if promo_orders:

        food_orders = {}
        drink_orders = {}
        add_on_quantity = 0

    else:

        food_orders = order_food()

        add_on_quantity = choose_add_on()

        drink_orders = order_beverages()

    subtotal = calculate_subtotal(
        food_orders,
        promo_orders,
        drink_orders,
        add_on_quantity
    )

    discount = choose_discount(subtotal)

    total = subtotal - discount

    while True:

        try:
            cash_received = float(
                input("Cash received: PHP ")
            )
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if cash_received >= total:
            break

        print("Insufficient cash.")

    change = cash_received - total

    print_ticket(
        food_orders,
        promo_orders,
        drink_orders,
        add_on_quantity,
        subtotal,
        discount,
        cash_received,
        total,
        change
    )


if __name__ == "__main__":
    main()