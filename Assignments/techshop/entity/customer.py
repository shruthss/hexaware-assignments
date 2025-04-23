# customer.py

class Customer:
    def __init__(self, firstname, lastname, email, phone, address, customerid=None):
        self.customerid = customerid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address = address

    def get_next_customerid(self, db_connector):
        # Get the last customer ID from the database and increment it by 1
        db_connector.cursor.execute("SELECT MAX(customerid) FROM customers")
        result = db_connector.cursor.fetchone()
        last_customerid = result[0] if result[0] else 0
        return last_customerid + 1

    def register_customer(self, db_connector):
        try:
            # Get the next customer ID
            self.customerid = self.get_next_customerid(db_connector)

            # Insert new customer with auto-incremented customerid
            db_connector.cursor.execute("""
                INSERT INTO customers (customerid, firstname, lastname, email, phone, address)
                VALUES (?, ?, ?, ?, ?, ?)
            """, self.customerid, self.firstname, self.lastname, self.email, self.phone, self.address)
            db_connector.connection.commit()
            print("Customer registered successfully.")
        except Exception as e:
            print(f"Error registering customer: {e}")
