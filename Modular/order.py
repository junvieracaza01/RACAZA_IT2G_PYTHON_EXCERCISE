from Modular.foodmenu import FOOD_MENU
from Modular.beverage import DRINK_MENU
from promos import PROMO_MENU
from Modular.cafeaddson import calculate_add_on_total


def calculate_subtotal(
    food_orders,
    promo_orders,
    drink_orders,
    add_on_quantity
):

    subtotal = 0

    for number, quantity in food_orders.items():

        price = FOOD_MENU[number][1]

        subtotal = subtotal + (price * quantity)

    for number, quantity in promo_orders.items():

        price = PROMO_MENU[number][1]

        subtotal = subtotal + (price * quantity)

    for number, quantity in drink_orders.items():

        price = DRINK_MENU[number][1]

        subtotal = subtotal + (price * quantity)

    subtotal = subtotal + calculate_add_on_total(
        add_on_quantity
    )

    return subtotal