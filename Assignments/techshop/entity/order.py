# order.py

class Order:
    def __init__(self, customerid, orderdate, totalamount, orderid=None):
        self.orderid = orderid
        self.customerid = customerid
        self.orderdate = orderdate
        self.totalamount = totalamount

    def get_next_orderid(self, db_connector):
        # Get the last order ID from the database and increment it by 1
        db_connector.cursor.execute("SELECT MAX(orderid) FROM orders")
        result = db_connector.cursor.fetchone()
        last_orderid = result[0] if result[0] else 0
        return last_orderid + 1

    def place_order(self, db_connector):
        try:
            # Get the next order ID
            self.orderid = self.get_next_orderid(db_connector)

            # Insert new order with auto-incremented orderid
            db_connector.cursor.execute("""
                INSERT INTO orders (orderid, customerid, orderdate, totalamount)
                VALUES (?, ?, ?, ?)
            """, self.orderid, self.customerid, self.orderdate, self.totalamount)
            db_connector.connection.commit()
            print("Order placed successfully.")
        except Exception as e:
            print(f"Error placing order: {e}")
