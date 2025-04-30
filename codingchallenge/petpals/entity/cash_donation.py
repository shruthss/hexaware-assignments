from entity.donation import Donation
from datetime import datetime
class CashDonation(Donation):
    def __init__(self,donor_name,amount,donation_date=None):
        super().__init__(donor_name,amount)
        self.donation_date=donation_date or datetime.now()
        
    def record_donation(self):
        print(f"Cash donation recorede from {self.donor_name} of{self.amount} on {self.donation_date.strftime('%y-%m-%d')}")
        