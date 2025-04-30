from abc import ABC,abstractmethod
class IAoptable(ABC):
    @abstractmethod
    def adopt(self):
        pass
class AdoptionEvent:
    def __init__(self):
        self.participants=[]
    def register_participants(self,participant:IAoptable):
        self.participants.append(participant)
    
    def host_event(self):
        print("Adoption Event Started:")
        for participant in self.participants:
            try:
                participant.adapt()
            except Exception as e:
                print(f"Error during adoption:{e}")