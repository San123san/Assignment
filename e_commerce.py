class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.orders = []  # List to hold active orders
        self.completed_orders = []  # List to hold completed orders
        self.all_orders = []  # List to hold all orders

    def login(self, email, password):
        return self.email == email and self.password == password

    def create_order(self):
        order = Order(self.user_id)
        self.orders.append(order)
        self.all_orders.append(order)
        return order
    
    def complete_order(self, order):
        self.completed_orders.append(order)  # Store completed order
        self.orders.remove(order)  # Remove from active orders


class Order:
    def __init__(self, user_id):
        self.order_id = id(self)  # Placeholder for a unique ID
        self.user_id = user_id
        self.status = 'pending'  # Order status
        self.products = []  # List of tuples (Product, Quantity)
        self.payment_status = 'pending'  # Payment status

    def add_product(self, product, quantity):
        self.products.append((product, quantity))  # Store product and quantity as a tuple

    def remove_product(self, product):
        self.products = [(p, qty) for p, qty in self.products if p.product_id != product.product_id]

    def update_quantity(self, product, quantity):
        for i, (p, qty) in enumerate(self.products):
            if p.product_id == product.product_id:
                if qty + quantity > 0:
                    self.products[i] = (p, qty + quantity)
                else:
                    self.remove_product(product)  # Remove the product if quantity goes to 0
                break

    def reset_cart(self):
        self.products.clear()  # Clear the cart
        self.payment_status = 'pending'  # Reset payment status
        self.status = 'pending'  # Reset order status

    def get_cart_summary(self):
        summary = []
        total_price = 0
        total_quantity = 0
        for product, quantity in self.products:
            item_total = product.price * quantity
            total_price += item_total
            total_quantity += quantity
            summary.append({
                "name": product.name,
                "quantity": quantity,
                "price": product.price,
                "total": item_total
            })
        return summary, total_price, total_quantity, self.payment_status  # Include payment status


class Payment:
    def __init__(self, order_id, amount, method):
        self.payment_id = id(self)  # Placeholder for a unique ID
        self.order_id = order_id
        self.amount = amount
        self.method = method
        self.status = 'pending'

    def process(self, order):  # Accept the order instance as a parameter
        self.status = 'completed'
        order.reset_cart()  # Reset the cart
        print(f"Payment processed for Order ID: {self.order_id} using {self.method}.")


class Product:
    def __init__(self, product_id, name, price, description, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock  # New attribute for stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def get_details(self):
        stock_status = "out of stock" if self.stock <= 0 else f"{self.stock} left"
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "stock": stock_status,
        }


# Main code
if __name__ == "__main__":
    users = []
    user_id_counter = 1  # To generate unique user IDs

    # Create a default user account
    default_user = User(user_id=user_id_counter, username="DefaultUser", email="default@example.com", password="defaultPassword123")
    users.append(default_user)
    user_id_counter += 1

    # Create product instances with stock information
    product1 = Product(product_id=1, name="Product 1", price=19.99, description="Description of Product 1", stock=5)
    product2 = Product(product_id=2, name="Product 2", price=29.99, description="Description of Product 2", stock=10)
    product3 = Product(product_id=3, name="Product 3", price=39.99, description="Description of Product 3", stock=2)
    product4 = Product(product_id=4, name="Product 4", price=49.99, description="Description of Product 4", stock=0)
    product5 = Product(product_id=5, name="Product 5", price=59.99, description="Description of Product 5", stock=1)

    products = [product1, product2, product3, product4, product5]

    current_user = None  # To track the logged-in user

    while True:
        print("\nE-Commerce System")
        print("1. Create User Account")
        print("2. Login (Default account available)")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")

            # Create new user
            new_user = User(user_id=user_id_counter, username=username, email=email, password=password)
            users.append(new_user)
            user_id_counter += 1
            print(f"User account created for {username}.")

        elif choice == '2':
            max_attempts = 3
            email_attempts = 0
            
            while email_attempts < max_attempts:
                email = input("Enter your email (default: default@example.com) or type 'cancel' to exit: ")
                if email.lower() == 'cancel':
                    print("Exiting login process.")
                    break

                current_user = next((u for u in users if u.email == email), None)

                if current_user is None:
                    email_attempts += 1
                    print(f"Incorrect email. You have {max_attempts - email_attempts} attempt(s) left.")
                else:
                    password_attempts = 0
                    while password_attempts < max_attempts:
                        password = input("Enter your password (default password: defaultPassword123) or type 'cancel' to exit: ")
                        if password.lower() == 'cancel':
                            print("Exiting login process.")
                            break

                        if current_user.login(email, password):
                            print(f"Welcome {current_user.username}!")
                            order = current_user.create_order()  # Create a new order for the user

                            while True:  # Keep this loop running until user logs out
                                print("\nWhat would you like to do?")
                                print("1. Add Product")
                                print("2. Remove Product")
                                print("3. Update Product Quantity")
                                print("4. View Cart")
                                print("5. Payment")
                                print("6. Check Order and Payment Status")
                                print("7. Logout")
                                print("8. Exit")
                                action_choice = input("Select an option: ")

                                if action_choice == '1':
                                    while True:
                                        print("\nAvailable Products:")
                                        for product in products:
                                            details = product.get_details()
                                            print(f"Product ID: {product.product_id}, Name: {details['name']}, Price: ${details['price']}, Stock: {details['stock']}")

                                        product_choice = input("Enter Product ID to add to order (or type 'cancel' to exit): ")
                                        if product_choice.lower() == 'cancel':
                                            break  # Exit the product selection loop

                                        if not product_choice.isdigit():
                                            print("Please enter a valid Product ID.")
                                            continue

                                        product_choice = int(product_choice)
                                        selected_product = next((p for p in products if p.product_id == product_choice), None)

                                        if not selected_product:
                                            print("This product is not available. Please enter another product ID.")
                                        else:
                                            if selected_product.stock <= 0:
                                                print(f"{selected_product.name} is out of stock.")
                                                continue

                                            while True:
                                                quantity = input(f"Enter quantity to add for {selected_product.name} (available: {selected_product.stock} or type 'cancel' to exit): ")
                                                if quantity.lower() == 'cancel':
                                                    break  # Exit quantity selection

                                                if not quantity.isdigit():
                                                    print("Please enter a valid number for quantity.")
                                                    continue

                                                quantity = int(quantity)
                                                if quantity <= 0:
                                                    print("Please enter a quantity greater than 0.")
                                                elif quantity > selected_product.stock:
                                                    print(f"Available stock for {selected_product.name} is {selected_product.stock}. Please enter a correct number of stock.")
                                                else:
                                                    order.add_product(selected_product, quantity)  # Add product and quantity
                                                    selected_product.update_stock(quantity)  # Decrease stock by the specified quantity
                                                    
                                                    # Show cart summary immediately after adding the product
                                                    cart_summary, total_price, total_quantity, payment_status = order.get_cart_summary()
                                                    print("\nUpdated Cart Summary:")
                                                    for item in cart_summary:
                                                        print(f"Order Name: {item['name']}, Quantity: {item['quantity']}, Price per unit: ${item['price']:.2f}, Total Price: ${item['total']:.2f}")
                                                    print(f"Total Quantity in Cart: {total_quantity}")
                                                    print(f"Total Amount to Pay: ${total_price:.2f}")
                                                    print(f"Payment Status: {payment_status}")  # Display payment status
                                                    break  # Exit the quantity loop

                                elif action_choice == '2':
                                    while True:
                                        if not order.products:
                                            print("Your cart is empty. No products to remove.")
                                            break

                                        print("\nProducts in Cart:")
                                        for item in order.products:
                                            product, qty = item
                                            print(f"Product ID: {product.product_id}, Name: {product.name}, Quantity: {qty}")

                                        product_choice = input("Enter Product ID to remove from order (or type 'cancel' to exit): ")
                                        if product_choice.lower() == 'cancel':
                                            break  # Exit the product removal loop

                                        if not product_choice.isdigit():
                                            print("Please enter a valid Product ID.")
                                            continue

                                        product_choice = int(product_choice)
                                        selected_product = next((p for p in order.products if p[0].product_id == product_choice), None)

                                        if not selected_product:
                                            print("This product is not in your cart. Please enter correct product ID.")
                                        else:
                                            product, qty = selected_product
                                            order.remove_product(product)
                                            product.update_stock(-qty)  # Restore stock
                                            print(f"Removed {product.name} from the cart.")
                                            break  # Exit the removal loop

                                elif action_choice == '3':
                                    if not order.products:
                                        print("Your cart is empty. No products to update.")
                                        continue

                                    while True:
                                        print("\nProducts in Cart:")
                                        for item in order.products:
                                            product, qty = item
                                            print(f"Product ID: {product.product_id}, Name: {product.name}, Quantity: {qty}")

                                        product_choice = input("Enter Product ID to update quantity (or type 'cancel' to exit): ")
                                        if product_choice.lower() == 'cancel':
                                            break

                                        if not product_choice.isdigit():
                                            print("Please enter a valid Product ID.")
                                            continue

                                        product_choice = int(product_choice)
                                        selected_product = next((p for p in order.products if p[0].product_id == product_choice), None)

                                        if not selected_product:
                                            print("This product is not in your cart. Please enter another product ID.")
                                        else:
                                            product, qty = selected_product
                                            new_quantity = input(f"Enter new quantity for {product.name} (current: {qty} or type 'cancel' to exit): ")
                                            if new_quantity.lower() == 'cancel':
                                                break

                                            if not new_quantity.isdigit() or int(new_quantity) < 0:
                                                print("Please enter a valid quantity greater than or equal to 0.")
                                                continue

                                            new_quantity = int(new_quantity)
                                            order.update_quantity(product, new_quantity - qty)  # Update quantity
                                            print(f"Updated quantity for {product.name}.")
                                            break  # Exit the update loop

                                elif action_choice == '4':
                                    cart_summary, total_price, total_quantity, payment_status = order.get_cart_summary()  # Get payment status
                                    print("\nCart Summary:")
                                    for item in cart_summary:
                                        print(f"Order Name: {item['name']}, Quantity: {item['quantity']}, Price per unit: ${item['price']:.2f}, Total Price: ${item['total']:.2f}")
                                    print(f"Total Quantity in Cart: {total_quantity}")
                                    print(f"Total Amount to Pay: ${total_price:.2f}")
                                    print(f"Payment Status: {payment_status}")  # Display payment status

                                elif action_choice == '5':
                                    cart_summary, total_price, total_quantity, payment_status = order.get_cart_summary()
                                    if total_quantity == 0:
                                        print("Your cart is empty. Please add products before proceeding to payment.")
                                        continue

                                    payment_method = input("Enter payment method (Credit/Debit/Cash): ")
                                    payment = Payment(order.order_id, total_price, payment_method)
                                    payment.process(order)  # Pass the order to the process method
                                    order.payment_status = 'completed'  # Update payment status
                                    order.status = 'completed'  # Update order status
                                    current_user.complete_order(order)  # Complete the order

                                    # Create a new order for subsequent purchases
                                    order = current_user.create_order()  # Create a new order for further actions

                                    print("Thank you for your purchase!")

                                elif action_choice == '6':
                                    completed_orders = [order for order in current_user.all_orders if order.status == 'completed']

                                    if not completed_orders:
                                        print("You have no orders.")
                                    else:
                                        print(f"Order Summary for {current_user.username}:")
                                        for order in completed_orders:
                                            print(f"Order ID: {order.order_id}, Order Status: {order.status}, Payment Status: {order.payment_status}")


                                elif action_choice == '7':
                                    print("Logging out...")
                                    current_user = None
                                    break  # Exit the user loop

                                elif action_choice == '8':
                                    print("Exiting the application.")
                                    exit(0)

                            break  # Break out of password attempts if logged in successfully
                    else:
                        print("Too many incorrect password attempts. Please try again later.")
                    break  # Break out of email attempts after finding the user

        elif choice == '3':
            print("Exiting the application.")
            break  # Exit the main loop

        else:
            print("Invalid choice. Please try again.")
