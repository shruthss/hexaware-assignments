class InvalidPetAgeException(Exception):
    def __init__(self,message="pet age must be positive"):
        super().__init__(message)