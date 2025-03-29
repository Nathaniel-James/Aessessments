class Product:
    stock = "items"

    def __init__(self, name, price, quantity):
        self.name = name  # name of the product
        self.price = price  # cost of the product
        self.quantity = quantity  # number of product available in stock

    def __str__(self):
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Availability:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def check_stock(self, product_name, quantity):
        product_name = product_name.title()  # Matches to dictionary

        if product_name not in self.product_catalog:
            return "Product not found."

        product = self.product_catalog[product_name]
        if product.quantity == 0:
            return f"{product_name} is **out of stock**."
        elif product.quantity < 5:
            return f"Low Stock Alert: Only {product.quantity} left!"
        elif quantity > product.quantity:
            return f"Only {product.quantity} {product_name}(s) available. Cannot add {quantity}."

        return f"{product_name} is available. ({product.quantity} in stock)"


class POS:
    def __init__(self):
        # The Product Storage
        self.products = {
            "Milk": Product("Milk", 150, 30),
            "Ketchup": Product("Ketchup", 200, 30),
            "Bread": Product("Bread", 800, 25),
            "Yoghurt": Product("Yoghurt", 350, 8),
            "Water": Product("Water", 100, 55),
            "Pepsi": Product("Pepsi", 300, 7),
            "Apple Juice": Product("Apple Juice", 300, 10),
            "Coke": Product("Coke", 200, 5),
            "Baking Soda": Product("Baking Soda", 300, 8),
            "Glass": Product("Glass", 600, 10),
            "Cutting Board": Product("Cutting Board", 300, 5),
            "Tin Cheese": Product("Tin Cheese", 650, 6),
            "Toothpaste": Product("Toothpaste", 250, 10),
            "Shampoo": Product("Shampoo", 300, 6),
            "Conditioner": Product("Conditioner", 300, 6),
        }
        self.cart = {}
        self.availability_checker = Availability(self.products)  # Passes products to Availability class

    def add_to_cart(self, product_name, quantity):
        product_name = product_name.title()
        stock_message = self.availability_checker.check_stock(product_name, quantity)

        if "Product not found" in stock_message or "Only" in stock_message:
            print(stock_message)
            return

        product = self.products[product_name]

        if product_name in self.cart:
            self.cart[product_name]["quantity"] += quantity
        else:
            self.cart[product_name] = {"price": product.price, "quantity": quantity}

        product.quantity -= quantity  # Takes from stock
        print(f"{quantity} {product_name}(s) added to cart. {product.quantity} remaining in stock.")

    def remove_from_cart(self, product_name, quantity):
        product_name = product_name.title()
        if product_name in self.cart:
            if quantity >= self.cart[product_name]["quantity"]:
                del self.cart[product_name]
            else:
                self.cart[product_name]["quantity"] -= quantity
                self.products[product_name].quantity += quantity
                print(f"{quantity} {product_name}(s) has been removed from cart")
        else:
            print("Item not in cart.")


    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("\n--- Shopping Cart ---")
            total = 0
            for item, details in self.cart.items():
                item_total = details["price"] * details["quantity"]
                total += item_total
                print(f"{item}: {details['quantity']} x ${details['price']} = ${item_total}")
            print(f"Subtotal is: ${total}")

    def checkout(self):
            if not self.cart:
                print("Car is empty. Cannot proceed to checkout.")
                return
            subtotal = sum(details["price"] * details["quantity"] for details in self.cart.values())
            tax = subtotal * 0.10
            total = subtotal + tax
            discount = 0
            if total > 5000:
                discount = total * 0.05
                print(f"Discount (5% over 5000): -${discount}")
            print(f"Total amount is: ${total}")
            while True:
                try:
                    amount_paid = float(input("Enter the amount Paid: "))
                    if amount_paid < total:
                        print("Insufficient payment. Try again.")
                    else:
                        change = amount_paid - total
                        print(f"change: ${change}")
                        self.generate_receipt(subtotal, tax, discount, total, amount_paid, change)
                        self.cart.clear()
                        break
                except ValueError:
                    print("Invalid input. Enter a valid amount.")

    def generate_receipt(self, subtotal, tax, discount, total, amount_paid, change):
           print("\n---- Receipt ----")
           print("Best Buy Retail Store")
           print("----------------------------------") #to add space to text
           for item, details in self.cart.items():
               item_total = details["price"] * details["quantity"]
               print(f"{item}: {details['quantity']} x ${details['price']} ${item_total}")
           print("----------------------------------")#to add space to text
           print(f"Subtotal: ${subtotal}")
           print(f"Sales Tax: ${tax}")
           if discount:
               print(f"Discount: -${discount}")
               print(f"Total: ${total}")
               print(f"Amount Paid: ${amount_paid}")
               print(f"Change ${change}")
               print("Thank you for shopping With Best Buy")


    def start(self):
            while True:
                print("\n--- Pos System Gang---")
                print("1. View Product")
                print("2. Add to cart")
                print("3. Remove from cart")
                print("4. View Cart")
                print("5. Checkout")
                print("6. Exit")
                choice = input("Select an option: ")

                if choice == "1":
                    for product in self.products.values():
                        print(product)
                elif choice == "2":
                    name = input("Enter product name: ")
                    try:
                        qty = int(input("Enter quantity: "))
                        self.add_to_cart(name, qty)
                    except ValueError:
                        print("Invalid quantity.")
                elif choice == "3":
                    name = input("Enter the product name: ")
                    try:
                        qty = int(input("Enter quantity: "))
                        self.remove_from_cart(name, qty)
                    except ValueError:
                        print("Invalid quantity")
                elif choice == "4":
                    self.view_cart()
                elif choice == "5":
                    self.checkout()
                elif choice == "6":
                    print("Exiting Pos System bye.")
                    break
                else:
                    print("Invalid option Entered.")

pos = POS()
pos.start()


