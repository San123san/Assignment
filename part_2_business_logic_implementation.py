class Inventory:
    def __init__(self):
        # Initialize an empty inventory
        self.stock = {}

    def load_inventory(self, products):
        """
        Load a list of products with their stock levels.
        
        Parameters:
        - products: List of tuples (product_name, stock_level)
        """
        for product_name, stock_level in products:
            self.stock[product_name] = stock_level

    def process_orders(self, orders, threshold=10):
        """
        Process a list of sales orders.
        
        Parameters:
        - orders: List of tuples (product_name, quantity)
        - threshold: Stock level below which a restock alert is triggered
        
        Returns:
        - List of products that need restocking
        """
        restock_alerts = []

        for product_name, quantity in orders:
            if product_name not in self.stock:
                raise ValueError(f"Product '{product_name}' does not exist in inventory.")
            
            if quantity > self.stock[product_name]:
                raise ValueError(f"Insufficient stock for '{product_name}'. Available: {self.stock[product_name]}, Requested: {quantity}.")
            
            # Reduce stock level
            self.stock[product_name] -= quantity

            # Check if stock is below threshold
            if self.stock[product_name] < threshold:
                restock_alerts.append(product_name)

        return restock_alerts

    def restock_items(self, restock_info):
        """
        Restock items based on a list of products and their required quantities.
        
        Parameters:
        - restock_info: List of tuples (product_name, quantity)
        """
        for product_name, quantity in restock_info:
            if product_name not in self.stock:
                raise ValueError(f"Product '{product_name}' does not exist in inventory.")
            
            self.stock[product_name] += quantity

# Driver code
if __name__ == "__main__":
    inventory = Inventory()
    
    initial_products = [("Widget A", 50), ("Widget B", 20), ("Widget C", 5)]
    inventory.load_inventory(initial_products)

    print("Initial stock levels:", inventory.stock)

    try:
        orders = [("Widget A", 10), ("Widget B", 15), ("Widget C", 3)]
        
        alerts = inventory.process_orders(orders)  
        print("Restock alerts for products:", alerts)

        print("Stock levels after processing orders:", inventory.stock)

        restock_info = [("Widget C", 10)]
        inventory.restock_items(restock_info)

        print("Updated stock levels after restocking:", inventory.stock)

    except ValueError as e:
        print("Error:", e)
restock_items(products, restock_quantities)

for product in products:
    print(product.name, product.stock_level)
