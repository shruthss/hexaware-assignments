import sys
import os

# Ensure the root directory is added to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Now safely import packages
try:
    from dao.service_provider_impl import ServiceProviderImpl
    from entity.cat import Cat
    from entity.dog import Dog
    from exception.adoption_exception import AdoptionException
    from exception.insufficient_fund_exception import InsufficientFundException
except ModuleNotFoundError as e:
    print("❌ Import error:", e)
    print("Please make sure your folder structure is correct and contains __init__.py files.")
    sys.exit(1)

def main():
    service = ServiceProviderImpl()

    while True:
        print("\n==== PET ADOPTION PLATFORM ====")
        print("1. Add Pet")
        print("2. List Available Pets")
        print("3. Remove Pet")
        print("4. Make Cash Donation")
        print("5. Host Adoption Event")
        print("6. Register Participant")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            try:
                pet_type = input("Enter pet type (dog/cat): ").lower()
                name = input("Enter pet name: ")
                age = int(input("Enter pet age: "))
                breed = input("Enter breed: ")

                if age <= 0:
                    raise ValueError("Age must be positive.")

                if pet_type == "dog":
                    dog_breed = input("Enter specific dog breed: ")
                    pet = Dog(name, age, breed, dog_breed)
                elif pet_type == "cat":
                    cat_color = input("Enter cat color: ")
                    pet = Cat(name, age, breed, cat_color)
                else:
                    print("❌ Invalid pet type.")
                    continue

                service.add_pet(pet)
                print("✅ Pet added successfully.")

            except ValueError as ve:
                print("❌ Invalid input:", ve)

        elif choice == '2':
            try:
                pets = service.list_available_pets()
                if not pets:
                    print("🚫 No pets available.")
                else:
                    for pet in pets:
                        print(pet)
            except Exception as e:
                print("❌ Error listing pets:", e)

        elif choice == '3':
            try:
                name = input("Enter name of the pet to remove: ")
                success = service.remove_pet(name)
                if success:
                    print("✅ Pet removed successfully.")
                else:
                    print("❌ Pet not found.")
            except Exception as e:
                print("❌ Error removing pet:", e)

        elif choice == '4':
            try:
                donor_name = input("Enter donor name: ")
                amount = float(input("Enter donation amount ($): "))
                if amount < 10:
                    raise InsufficientFundException("Minimum donation is $10.")
                service.make_cash_donation(donor_name, amount)
                print("✅ Donation recorded. Thank you!")

            except InsufficientFundException as ie:
                print("❌", ie)
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == '5':
            try:
                service.host_adoption_event()
            except Exception as e:
                print("❌ Error hosting event:", e)

        elif choice == '6':
            try:
                participant_name = input("Enter participant name (shelter or adopter): ")
                service.register_participant(participant_name)
                print("✅ Participant registered.")
            except AdoptionException as ae:
                print("❌", ae)

        elif choice == '7':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
