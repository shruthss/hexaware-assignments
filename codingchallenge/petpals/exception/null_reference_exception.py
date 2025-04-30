class NullRefernceException(Exception):
    def __init__(self,message="attempted to access a property of null object"):
        super().__init__(message)