class AdoptionException(Exception):
    def __init__(self,message="adoption failed"):
        super().__init__(message)