# class Inventory:
#     def __init__(self):
#         # Initialize an empty inventory
#         self.stock = {}

#     def load_inventory(self, products):
#         """
#         Load a list of products with their stock levels.
        
#         Parameters:
#         - products: List of tuples (product_name, stock_level)
#         """
#         for product_name, stock_level in products:
#             self.stock[product_name] = stock_level

#     def process_orders(self, orders, threshold=10):
#         """
#         Process a list of sales orders.
        
#         Parameters:
#         - orders: List of tuples (product_name, quantity)
#         - threshold: Stock level below which a restock alert is triggered
        
#         Returns:
#         - List of products that need restocking
#         """
#         restock_alerts = []

#         for product_name, quantity in orders:
#             if product_name not in self.stock:
#                 raise ValueError(f"Product '{product_name}' does not exist in inventory.")
            
#             if quantity > self.stock[product_name]:
#                 raise ValueError(f"Insufficient stock for '{product_name}'. Available: {self.stock[product_name]}, Requested: {quantity}.")
            
#             # Reduce stock level
#             self.stock[product_name] -= quantity

#             # Check if stock is below threshold
#             if self.stock[product_name] < threshold:
#                 restock_alerts.append(product_name)

#         return restock_alerts

#     def restock_items(self, restock_info):
#         """
#         Restock items based on a list of products and their required quantities.
        
#         Parameters:
#         - restock_info: List of tuples (product_name, quantity)
#         """
#         for product_name, quantity in restock_info:
#             if product_name not in self.stock:
#                 raise ValueError(f"Product '{product_name}' does not exist in inventory.")
            
#             # Update stock level
#             self.stock[product_name] += quantity

# # Driver code to demonstrate functionality
# if __name__ == "__main__":
#     # Initialize inventory
#     inventory = Inventory()
    
#     # Load initial stock levels from a list of products
#     initial_products = [("Widget A", 50), ("Widget B", 20), ("Widget C", 5)]
#     inventory.load_inventory(initial_products)

#     print("Initial stock levels:", inventory.stock)

#     try:
#         # List of incoming sales orders
#         orders = [("Widget A", 10), ("Widget B", 15), ("Widget C", 3)]
        
#         # Process orders
#         alerts = inventory.process_orders(orders)  # Uses the incoming sales orders
#         print("Restock alerts for products:", alerts)

#         # Check stock levels after processing orders
#         print("Stock levels after processing orders:", inventory.stock)

#         # Restocking products that need it
#         restock_info = [("Widget C", 10)]
#         inventory.restock_items(restock_info)

#         # Verify stock levels after restocking
#         print("Updated stock levels after restocking:", inventory.stock)

#     except ValueError as e:
#         print("Error:", e)


class Product:
    def __init__(self, name, stock_level):
        self.name = name
        self.stock_level = stock_level

class Order:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity

def process_orders(products, orders):
    """
    Processes incoming sales orders and updates product stock levels.

    Args:
        products: A list of Product objects representing the available products.
        orders: A list of Order objects representing the incoming sales orders.
    """
    for order in orders:
        for product in products:
            if product.name == order.product_name:
                product.stock_level -= order.quantity
                if product.stock_level < 10:
                    print(f"Low stock alert for {product.name}.")
                break
        else:
            print(f"Error: Product {order.product_name} not found.")

def restock_items(products, restock_quantities):
    """
    Restocks products based on the specified quantities.

    Args:
        products: A list of Product objects representing the available products.
        restock_quantities: A dictionary mapping product names to their required restock quantities.
    """
    for product, quantity in restock_quantities.items():
        for p in products:
            if p.name == product:
                p.stock_level += quantity
                break
        else:
            print(f"Error: Product {product} not found.")

# Example usage
products = [
    Product("Laptop", 20),
    Product("Phone", 15),
    Product("Tablet", 8)
]

orders = [
    Order("Laptop", 5),
    Order("Phone", 10),
    Order("Tablet", 3)
]

restock_quantities = {
    "Laptop": 10,
    "Phone": 5
}

process_orders(products, orders)
restock_items(products, restock_quantities)

# Print the updated products with their names and stock levels
for product in products:
    print(product.name, product.stock_level)