import pyodbc
from util.property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(property_file="config.properties"):
        try:
            conn_str = DBPropertyUtil.get_connection_string(property_file)
            conn = pyodbc.connect(conn_str)
            return conn
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            return None