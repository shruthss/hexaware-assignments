from entity.donation import Donation
class ItemDonation(Donation):
    def __init__(self,donar_name,amount,item_type):
        super().__init__(donor_name,amount)
        self.item_type=item_type
    
    def record_donation(self):
        print(f"item recorded from {self.donor_name}: {self.item_type} valued at{self.amount}")