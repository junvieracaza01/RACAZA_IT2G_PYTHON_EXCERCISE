from cafe import Cafe


cafe = Cafe()


print("=" * 50)
print("                    JUN'S CAFE")
print("=" * 50)
print("                  WELCOME!")
print("=" * 50)


# ==========================================
# START ORDER
# ==========================================

while True:

    try:

        start = int(
            input("Enter 1 to start your order: ")
        )

    except ValueError:

        print("Please enter a valid number.")
        continue

    if start == 1:

        break

    print("Please enter 1.")


# ==========================================
# PROMO
# ==========================================

has_promo = cafe.order_promo()


# ==========================================
# IF NO PROMO
# ==========================================

if has_promo == False:

    # FOOD
    cafe.order_food()

    # ADD-ON
    cafe.order_addon()

    # BEVERAGE
    cafe.order_beverage()


# ==========================================
# CALCULATIONS
# ==========================================

cafe.calculate_subtotal()

cafe.calculate_discount()

cafe.calculate_total()


# ==========================================
# PAYMENT
# ==========================================

cafe.payment()


# ==========================================
# PRINT RECEIPT
# ==========================================

cafe.print_ticket()