from Modular.foodmenu import FOOD_MENU
from Modular.beverage import DRINK_MENU
from Modular.promos import PROMO_MENU
from Modular.cafeaddson import ADD_ON_NAME, ADD_ON_PRICE


def print_ticket(
    food_orders,
    promo_orders,
    drink_orders,
    add_on_quantity,
    subtotal,
    discount,
    cash_received,
    total,
    change
):

    print("=" * 48)
    print("                    JUN'S CAFE")
    print("=" * 48)

    print(
        "| NO. | FOOD & BEVERAGE               "
        "| QTY | TOTAL      |"
    )

    print(
        "|-----|-------------------------------"
        "|-----|------------|"
    )

    for number, quantity in food_orders.items():

        name = FOOD_MENU[number][0]
        price = FOOD_MENU[number][1]

        item_total = price * quantity

        print(
            f"| {number:>3} | "
            f"{name:<29} | "
            f"{quantity:>3} | "
            f"PHP {item_total:>7.2f} |"
        )

    for number, quantity in promo_orders.items():

        name = PROMO_MENU[number][0]
        price = PROMO_MENU[number][1]

        item_total = price * quantity

        print(
            f"| P{number:>2} | "
            f"{name:<29} | "
            f"{quantity:>3} | "
            f"PHP {item_total:>7.2f} |"
        )

    if add_on_quantity > 0:

        add_on_total = ADD_ON_PRICE * add_on_quantity

        print(
            f"| AD  | "
            f"{ADD_ON_NAME:<29} | "
            f"{add_on_quantity:>3} | "
            f"PHP {add_on_total:>7.2f} |"
        )

    for number, quantity in drink_orders.items():

        name = DRINK_MENU[number][0]
        price = DRINK_MENU[number][1]

        item_total = price * quantity

        print(
            f"| D{number:>2} | "
            f"{name:<29} | "
            f"{quantity:>3} | "
            f"PHP {item_total:>7.2f} |"
        )

    print(
        "|-----|-------------------------------"
        "|-----|------------|"
    )

    print(
        "|     | Subtotal                      "
        f"|     | PHP {subtotal:>7.2f} |"
    )

    print(
        "|     | Cash Received                 "
        f"|     | PHP {cash_received:>7.2f} |"
    )

    print(
        "|     | Change                        "
        f"|     | PHP {change:>7.2f} |"
    )

    print(
        "|     | Discount                      "
        f"|     | PHP {discount:>7.2f} |"
    )

    print(
        "|-----|-------------------------------"
        "|-----|------------|"
    )

    print(
        "|     | TOTAL                         "
        f"|     | PHP {total:>7.2f} |"
    )

    print(
        "|-----|-------------------------------"
        "|-----|------------|"
    )

    print(
        "|           THANK YOU FOR ORDERING!              |"
    )

    print(
        "|              PLEASE COME AGAIN!                |"
    )

    print("=" * 48)s