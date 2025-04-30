class Petshelter:
    def __init__(self):
        self_available_pets=[]
    def add_pet(self,pet):
        self.available_pets.append(pet)
    def remove_pet(self,pet):
        self.available_pets.remove(pet)
    def list_available_pets(self):
        for pets in self.available_pets:
            print(pet)