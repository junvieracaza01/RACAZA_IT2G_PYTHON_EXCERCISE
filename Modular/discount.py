def choose_discount(subtotal):

    print("=" * 48)
    print("                  DISCOUNT")
    print("=" * 48)
    print("| NO. | DISCOUNT TYPE                  |")
    print("|-----|-------------------------------|")
    print("|   1 | NONE                          |")
    print("|   2 | SENIOR CITIZEN                |")
    print("|   3 | PWD                           |")
    print("|-----|-------------------------------|")

    try:
        choice = int(input("Enter discount number: "))
    except ValueError:
        print("Invalid discount number.")
        return 0

    if choice == 1:

        return 0

    elif choice == 2:

        return subtotal * 0.20

    elif choice == 3:

        return subtotal * 0.20

    else:

        print("Invalid discount number.")
        return 0