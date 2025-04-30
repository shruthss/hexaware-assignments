import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            conn = pyodbc.connect(
                r'DRIVER={ODBC Driver 17 for SQL Server};'
                r'SERVER=SHRUTHI;'  
                r'DATABASE=petpals;'            
                r'Trusted_Connection=yes;'
            )
            print("✅ Connected to the database successfully.")
            return conn
        except pyodbc.Error as e:
            print("❌ Database connection error:", e)
            return None
