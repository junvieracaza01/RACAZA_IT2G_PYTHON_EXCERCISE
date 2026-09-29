class Cafe:

    def __init__(self):

        # ==============================
        # FOOD MENU
        # ==============================

        self.food_menu = {
            1: ["Burger", 120],
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
            16: ["Cookies", 50]
        }

        # ==============================
        # BEVERAGE MENU
        # ==============================

        self.beverage_menu = {
            1: ["Iced Coffee", 90],
            2: ["Hot Coffee", 80],
            3: ["Cappuccino", 110],
            4: ["Cafe Latte", 110],
            5: ["Caramel Macchiato", 120],
            6: ["Chocolate Milkshake", 130],
            7: ["Bottled Water", 30]
        }

        # ==============================
        # PROMO MENU
        # ==============================

        self.promo_menu = {
            1: ["Coffee and Cake", 180],
            2: ["Burger and Fries", 180],
            3: ["Pasta and Drink", 200],
            4: ["Family Cafe Promo", 450]
        }

        # ==============================
        # ADD-ON
        # ==============================

        self.addon_name = "Extra Whipped Cream"
        self.addon_price = 30

        # ==============================
        # ORDERS
        # ==============================

        self.food_orders = {}
        self.beverage_orders = {}
        self.promo_orders = {}

        self.addon_quantity = 0

        # ==============================
        # PAYMENT
        # ==============================

        self.subtotal = 0
        self.discount = 0
        self.total = 0
        self.cash = 0
        self.change = 0


    # ==================================================
    # FOOD MENU
    # ==================================================

    def show_food_menu(self):

        print()
        print("=" * 50)
        print("                    FOOD MENU")
        print("=" * 50)

        print("| No. | Food                         | Price     |")
        print("|-----|------------------------------|-----------|")

        for number, item in self.food_menu.items():

            print(
                f"| {number:>3} | "
                f"{item[0]:<28} | "
                f"PHP {item[1]:>7.2f} |"
            )

        print("=" * 50)


    def order_food(self):

        while True:

            self.show_food_menu()

            try:

                choice = int(
                    input("Enter food number: ")
                )

                quantity = int(
                    input("Enter quantity: ")
                )

            except ValueError:

                print("Please enter a valid number.")
                continue

            if choice not in self.food_menu:

                print("Invalid food number.")
                continue

            if quantity <= 0:

                print("Quantity must be greater than 0.")
                continue

            if choice in self.food_orders:

                self.food_orders[choice] += quantity

            else:

                self.food_orders[choice] = quantity

            print(
                quantity,
                "x",
                self.food_menu[choice][0],
                "added."
            )

            another = input(
                "Do you want another food? (yes/no): "
            ).lower()

            if another == "no":

                break


    # ==================================================
    # PROMO
    # ==================================================

    def show_promos(self):

        print()
        print("=" * 50)
        print("                   PROMOS")
        print("=" * 50)

        print("| No. | Promo                        | Price     |")
        print("|-----|------------------------------|-----------|")

        for number, item in self.promo_menu.items():

            print(
                f"| {number:>3} | "
                f"{item[0]:<28} | "
                f"PHP {item[1]:>7.2f} |"
            )

        print("|   0 | No Promo                     |           |")
        print("=" * 50)


    def order_promo(self):

        self.show_promos()

        try:

            choice = int(
                input("Enter promo number: ")
            )

        except ValueError:

            print("Invalid input.")
            return False

        if choice == 0:

            print("No promo selected.")
            return False

        if choice not in self.promo_menu:

            print("Invalid promo number.")
            return False

        try:

            quantity = int(
                input("Enter quantity: ")
            )

        except ValueError:

            print("Invalid quantity.")
            return False

        if quantity <= 0:

            print("Quantity must be greater than 0.")
            return False

        self.promo_orders[choice] = quantity

        print(
            quantity,
            "x",
            self.promo_menu[choice][0],
            "added."
        )

        return True


    # ==================================================
    # ADD-ONS
    # ==================================================

    def show_addons(self):

        print()
        print("=" * 50)
        print("                  ADD-ONS")
        print("=" * 50)

        print("| No. | Add-on                       | Price     |")
        print("|-----|------------------------------|-----------|")
        print("|   1 | Extra Whipped Cream          | PHP 30.00 |")
        print("|   2 | No Add-on                    | PHP  0.00 |")

        print("=" * 50)


    def order_addon(self):

        self.show_addons()

        try:

            choice = int(
                input("Enter choice: ")
            )

        except ValueError:

            print("Invalid input.")
            return

        if choice == 1:

            try:

                quantity = int(
                    input("Enter quantity: ")
                )

            except ValueError:

                print("Invalid quantity.")
                return

            if quantity > 0:

                self.addon_quantity = quantity

                print(
                    quantity,
                    "x",
                    self.addon_name,
                    "added."
                )

            else:

                print("Invalid quantity.")

        elif choice == 2:

            self.addon_quantity = 0

            print("No add-on selected.")

        else:

            print("Invalid choice.")


    # ==================================================
    # BEVERAGE MENU
    # ==================================================

    def show_beverage_menu(self):

        print()
        print("=" * 50)
        print("                 BEVERAGE MENU")
        print("=" * 50)

        print("| No. | Beverage                     | Price     |")
        print("|-----|------------------------------|-----------|")

        for number, item in self.beverage_menu.items():

            print(
                f"| {number:>3} | "
                f"{item[0]:<28} | "
                f"PHP {item[1]:>7.2f} |"
            )

        print("|   0 | No Beverage                  |           |")
        print("=" * 50)


    def order_beverage(self):

        while True:

            self.show_beverage_menu()

            try:

                choice = int(
                    input("Enter beverage number: ")
                )

            except ValueError:

                print("Please enter a valid number.")
                continue

            if choice == 0:

                break

            if choice not in self.beverage_menu:

                print("Invalid beverage number.")
                continue

            try:

                quantity = int(
                    input("Enter quantity: ")
                )

            except ValueError:

                print("Please enter a valid quantity.")
                continue

            if quantity <= 0:

                print("Quantity must be greater than 0.")
                continue

            if choice in self.beverage_orders:

                self.beverage_orders[choice] += quantity

            else:

                self.beverage_orders[choice] = quantity

            print(
                quantity,
                "x",
                self.beverage_menu[choice][0],
                "added."
            )

            another = input(
                "Do you want another beverage? (yes/no): "
            ).lower()

            if another == "no":

                break


    # ==================================================
    # CALCULATE SUBTOTAL
    # ==================================================

    def calculate_subtotal(self):

        self.subtotal = 0

        # FOOD
        for number, quantity in self.food_orders.items():

            price = self.food_menu[number][1]

            self.subtotal += price * quantity

        # PROMO
        for number, quantity in self.promo_orders.items():

            price = self.promo_menu[number][1]

            self.subtotal += price * quantity

        # BEVERAGE
        for number, quantity in self.beverage_orders.items():

            price = self.beverage_menu[number][1]

            self.subtotal += price * quantity

        # ADD-ON
        self.subtotal += (
            self.addon_price *
            self.addon_quantity
        )

        return self.subtotal


    # ==================================================
    # DISCOUNT
    # ==================================================

    def show_discount(self):

        print()
        print("=" * 50)
        print("                  DISCOUNT")
        print("=" * 50)

        print("| No. | Discount Type               |")
        print("|-----|-----------------------------|")
        print("|   1 | No Discount                 |")
        print("|   2 | Senior Citizen - 20%       |")
        print("|   3 | PWD - 20%                  |")

        print("=" * 50)


    def calculate_discount(self):

        self.show_discount()

        try:

            choice = int(
                input("Enter discount number: ")
            )

        except ValueError:

            print("Invalid input.")

            self.discount = 0

            return

        if choice == 1:

            self.discount = 0

        elif choice == 2:

            self.discount = self.subtotal * 0.20

        elif choice == 3:

            self.discount = self.subtotal * 0.20

        else:

            print("Invalid discount number.")

            self.discount = 0


    # ==================================================
    # TOTAL
    # ==================================================

    def calculate_total(self):

        self.total = (
            self.subtotal -
            self.discount
        )

        return self.total


    # ==================================================
    # PAYMENT
    # ==================================================

    def payment(self):

        while True:

            try:

                self.cash = float(
                    input("Cash received: PHP ")
                )

            except ValueError:

                print("Please enter a valid amount.")
                continue

            if self.cash < self.total:

                print("Insufficient cash.")

            else:

                self.change = (
                    self.cash -
                    self.total
                )

                break


    # ==================================================
    # PRINT TICKET
    # ==================================================

    def print_ticket(self):

        print()
        print("=" * 50)
        print("                    JUN'S CAFE")
        print("=" * 50)

        print("| No. | Item                         | Qty | Total     |")
        print("|-----|------------------------------|-----|-----------|")

        # FOOD
        for number, quantity in self.food_orders.items():

            name = self.food_menu[number][0]
            price = self.food_menu[number][1]

            total = price * quantity

            print(
                f"| {number:>3} | "
                f"{name:<28} | "
                f"{quantity:>3} | "
                f"PHP {total:>7.2f} |"
            )

        # PROMO
        for number, quantity in self.promo_orders.items():

            name = self.promo_menu[number][0]
            price = self.promo_menu[number][1]

            total = price * quantity

            print(
                f"| P{number:>2} | "
                f"{name:<28} | "
                f"{quantity:>3} | "
                f"PHP {total:>7.2f} |"
            )

        # BEVERAGE
        for number, quantity in self.beverage_orders.items():

            name = self.beverage_menu[number][0]
            price = self.beverage_menu[number][1]

            total = price * quantity

            print(
                f"| B{number:>2} | "
                f"{name:<28} | "
                f"{quantity:>3} | "
                f"PHP {total:>7.2f} |"
            )

        # ADD-ON
        if self.addon_quantity > 0:

            total = (
                self.addon_price *
                self.addon_quantity
            )

            print(
                f"| AD  | "
                f"{self.addon_name:<28} | "
                f"{self.addon_quantity:>3} | "
                f"PHP {total:>7.2f} |"
            )

        print("|-----|------------------------------|-----|-----------|")

        print(
            f"|     | Subtotal                     |     | "
            f"PHP {self.subtotal:>7.2f} |"
        )

        print(
            f"|     | Discount                     |     | "
            f"PHP {self.discount:>7.2f} |"
        )

        print(
            f"|     | TOTAL                        |     | "
            f"PHP {self.total:>7.2f} |"
        )

        print(
            f"|     | Cash                         |     | "
            f"PHP {self.cash:>7.2f} |"
        )

        print(
            f"|     | Change                       |     | "
            f"PHP {self.change:>7.2f} |"
        )

        print("|-----|------------------------------|-----|-----------|")

        print()
        print("             THANK YOU FOR ORDERING!")
        print("                 PLEASE COME AGAIN!")
        print()

        print("=" * 50)