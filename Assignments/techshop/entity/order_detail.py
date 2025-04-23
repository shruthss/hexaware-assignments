class OrderDetail:
    def __init__(self, orderid, productid, quantity, orderdetailid=None):
        self.orderdetailid = orderdetailid
        self.orderid = orderid
        self.productid = productid
        self.quantity = quantity

    def get_next_orderdetailid(self, db_connector):
        # Query the maximum current orderdetailid in the orderdetails table and increment by 1
        db_connector.cursor.execute("SELECT MAX(orderdetailid) FROM orderdetails")
        result = db_connector.cursor.fetchone()
        return result[0] + 1 if result[0] is not None else 1

    def validate_productid(self, db_connector):
        # Check if productid exists in the products table
        db_connector.cursor.execute("SELECT COUNT(*) FROM products WHERE productid = ?", (self.productid,))
        result = db_connector.cursor.fetchone()
        if result[0] == 0:
            raise ValueError(f"Product ID {self.productid} does not exist in the products table.")

    def add_order_detail(self, db_connector):
        try:
            # Validate productid before inserting order detail
            self.validate_productid(db_connector)

            # Get the next orderdetail ID if it's not auto-incremented
            if not self.orderdetailid:
                self.orderdetailid = self.get_next_orderdetailid(db_connector)

            # Insert order details into the orderdetails table
            db_connector.cursor.execute("""
                INSERT INTO orderdetails (orderdetailid, orderid, productid, quantity)
                VALUES (?, ?, ?, ?)
            """, self.orderdetailid, self.orderid, self.productid, self.quantity)
            db_connector.connection.commit()
            print("Order detail added successfully.")
        except Exception as e:
            print(f"Error adding order detail: {e}")
