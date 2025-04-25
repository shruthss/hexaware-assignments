# main.py

from entity.customer import Customer
from entity.product import Product
from entity.order import Order
from entity.order_detail import OrderDetail  # Ensure this is correct path
from database_connector import DatabaseConnector

def main():
    # Connect to the database
    db_connector = DatabaseConnector()
    db_connector.connect()

    # Register a new customer
    print("--- Customer Registration ---")
    new_customer = Customer("John", "Doe", "john.doe@example.com", "1234567890", "123 Main St, chennai, india")
    new_customer.register_customer(db_connector)  # Register customer in the database

    # Register a new product
    print("\n--- Product Registration ---")
    new_product = Product("Laptop", "A high-performance laptop", 1000.00)
    new_product.register_product(db_connector)  # Register product in the database

    # Place a new order
    print("\n--- Order Placement ---")
    order = Order(new_customer.customerid, "2025-04-23", 1000.00)  # Use customer ID from registered customer
    order.place_order(db_connector)  # Place the order in the database

    # Add order details
    print("\n--- Adding Order Details ---")
    order_detail = OrderDetail(order.orderid, new_product.productid, 1)  # Use order and product IDs from inserted records
    order_detail.add_order_detail(db_connector)  # Add order details in the database

    # Close the database connection
    db_connector.close()

if __name__ == "__main__":
    main()
