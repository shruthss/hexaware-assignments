class InsufficientFundException(Exception):
    def __init__(self,message=" donation amount is below the minimum"):
        super().__init__(message)