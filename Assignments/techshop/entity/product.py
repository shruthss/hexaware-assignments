class Product:
    def __init__(self, productname, description, price, productid=None):
        self.productid = productid
        self.productname = productname
        self.description = description
        self.price = price

    def get_next_productid(self, db_connector):
        # Query the maximum current productid in the products table and increment by 1
        db_connector.cursor.execute("SELECT MAX(productid) FROM products")
        result = db_connector.cursor.fetchone()
        return result[0] + 1 if result[0] is not None else 1

    def register_product(self, db_connector):
        try:
            # Get the next product ID
            self.productid = self.get_next_productid(db_connector)

            # Insert new product with the next productid
            db_connector.cursor.execute("""
                INSERT INTO products (productid, productname, description, price)
                VALUES (?, ?, ?, ?)
            """, self.productid, self.productname, self.description, self.price)
            db_connector.connection.commit()
            print("Product registered successfully.")
        except Exception as e:
            print(f"Error registering product: {e}")
