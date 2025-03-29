#Caclulator Menu Program
#Adams and James
# To calculate simple shape's areas with user-friendly prompts


option = 0
while option != 5:
    print("\nMenu:")
    print("1. Calculate area of a Triangle")
    print("2. Calculate area of a Square")
    print("3. Calculate area of a Rectangle")
    print("4. Calculate area of a Trapezium")
    print("5. Exit")

    # Get valid option
    while True:
        try:
            option = int(input("Enter your choice (1-5): "))
            if 1 <= option <= 5:
                break
            else:
                print("Invalid Option. Please Choose a valid option.")
        except ValueError:
            print("Invalid Input! \nPlease enter a numeric value.")

    # Get triangle area
    if option == 1:

        while True:
            try:
                base = float(input("Enter the base of the triangle: "))
                if base > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        while True:
            try:
                height = float(input("Enter the height of the triangle: "))
                if height > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        area = 0.5 * base * height
        print(f"The area of the Triangle is: {int(area)} m^2")

    # Get square sides
    elif option == 2:

        while True:
            try:
                side = float(input("Enter the sides of the square: "))
                if side > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        area = side * side
        print(f"The area of the Square is: {int(area)} m^2")

    # Get rectangle area
    elif option == 3:

        while True:
            try:
                length = float(input("Enter the length of the rectangle: "))
                if length > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        while True:
            try:
                width = float(input("Enter the width of the rectangle: "))
                if width > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        area = length * width
        print(f"The area of the Rectangle is: {int(area)} m^2")

    # Get trapezium area
    elif option == 4:

        while True:
            try:
                base1 = float(input("Enter the first base of the trapezium: "))
                if base1 > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        while True:
            try:
                base2 = float(input("Enter the second base of the trapezium: "))
                if base2 > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        while True:
            try:
                height = float(input("Enter the Height of the trapezium: "))
                if height > 0:
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! \nPlease enter a numeric value.")

        area = 0.5 * (base1 + base2) * height
        print(f"The area of the Trapezium is: {int(area)} m^2")

    # Exit Program if user selects 5
    elif option == 5:

        print("Exiting Menu")
        break


    # Ask user if they want to continue using the Calculator
    while True:
        print("\nAny other calculation? 1. YES 2. NO")
        continue_choice = input("Enter choice (1 for YES, 2 for NO): ").strip().upper()

        if continue_choice in ('1', 'YES'):
            print("Returning to Menu...")
            break
        elif continue_choice in ('2', 'NO'):
            print("Exiting Menu...")
            exit()
        else:
            print("Invalid input! Please enter '1' or 'YES' for YES, or '2' or 'NO' for NO.")
