class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file="config.properties"):
        return (
            "DRIVER={SQL Server};"
            "SERVER=SHRUTHI;"
            "DATABASE=fin;"
            "Trusted_Connection=yes;"
        )