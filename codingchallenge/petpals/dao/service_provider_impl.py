import pyodbc
from dao.i_service_provider import IServiceProvider
from util.db_conn_util import DBConnUtil
from exception.insufficient_fund_exception import InsufficientFundException
from entity.pet import Pet
from entity.cash_donation import CashDonation
from entity.item_donation import ItemDonation
from entity.adoption_event import AdoptionEvent


class ServiceProviderImpl(IServiceProvider):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    # ---------- Pet Management ----------
    def add_pet(self, pet: Pet):
        try:
            if pet.get_age() <= 0:
                raise ValueError("Pet age must be a positive integer.")
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO pets (name, age, breed) VALUES (?, ?, ?)",
                        pet.get_name(), pet.get_age(), pet.get_breed())
            self.conn.commit()
            print("Pet added successfully.")
        except Exception as e:
            print(f"Error adding pet: {e}")

    def remove_pet(self, pet_id: int):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM pets WHERE id = ?", pet_id)
            self.conn.commit()
            print("Pet removed successfully.")
        except Exception as e:
            print(f"Error removing pet: {e}")

    def list_available_pets(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, name, age, breed FROM pets")
            pets = cursor.fetchall()
            for pet in pets:
                print(f"ID: {pet.id}, Name: {pet.name}, Age: {pet.age}, Breed: {pet.breed}")
        except Exception as e:
            print(f"Error listing pets: {e}")

    # ---------- Donation Handling ----------
    def record_donation(self, donation):
        try:
            if donation.amount < 10:
                raise InsufficientFundException()
            cursor = self.conn.cursor()
            if isinstance(donation, CashDonation):
                cursor.execute("""
                    INSERT INTO donations (donor_name, amount, donation_date, donation_type)
                    VALUES (?, ?, ?, ?)
                """, donation.donor_name, donation.amount, donation.donation_date, 'Cash')
            elif isinstance(donation, ItemDonation):
                cursor.execute("""
                    INSERT INTO donations (donor_name, amount, item_type, donation_type)
                    VALUES (?, ?, ?, ?)
                """, donation.donor_name, donation.amount, donation.item_type, 'Item')
            else:
                raise ValueError("Unsupported donation type.")
            self.conn.commit()
            print("Donation recorded successfully.")
        except InsufficientFundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error recording donation: {e}")

    def list_donations(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM donations")
            donations = cursor.fetchall()
            for d in donations:
                print(d)
        except Exception as e:
            print(f"Error listing donations: {e}")

    # ---------- Adoption Event Management ----------
    def register_for_event(self, participant):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO participants (name) VALUES (?)", participant)
            self.conn.commit()
            print("Participant registered successfully.")
        except Exception as e:
            print(f"Error registering participant: {e}")

    def host_adoption_event(self, event: AdoptionEvent):
        try:
            print("Hosting adoption event...")
            event.host_event()
            print("Adoption event completed.")
        except Exception as e:
            print(f"Error hosting adoption event: {e}")

    def list_events(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM adoption_events")
            events = cursor.fetchall()
            for e in events:
                print(e)
        except Exception as e:
            print(f"Error listing events: {e}")
