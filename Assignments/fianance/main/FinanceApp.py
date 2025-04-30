import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))


from dao.finance_repository_impl import FinanceRepositoryImpl
from entity.user import User
from entity.expense import Expense

repo = FinanceRepositoryImpl()

def main():
    while True:
        print("\n1. Add User\n2. Add Expense\n3. Delete User\n4. Delete Expense\n5. Update Expense\n6. View Expenses\n0. Exit")
        ch = input("Choose: ")

        try:
            if ch == "1":
                u = User(username=input("Username: "), password=input("Password: "), email=input("Email: "))
                repo.create_user(u)

            elif ch == "2":
                e = Expense(user_id=int(input("User ID: ")), amount=float(input("Amount: ")),
                            category_id=int(input("Category ID: ")), date=input("Date: "), description=input("Desc: "))
                repo.create_expense(e)

            elif ch == "3":
                repo.delete_user(int(input("User ID: ")))

            elif ch == "4":
                repo.delete_expense(int(input("Expense ID: ")))

            elif ch == "5":
                eid = int(input("Expense ID: "))
                uid = int(input("User ID: "))
                amt = float(input("New Amount: "))
                cid = int(input("Category ID: "))
                date = input("Date: ")
                desc = input("Desc: ")
                e = Expense(expense_id=eid, user_id=uid, amount=amt, category_id=cid, date=date, description=desc)
                repo.update_expense(uid, e)

            elif ch == "6":
                uid = int(input("User ID: "))
                for row in repo.get_all_expenses(uid):
                    print(row)

            elif ch == "0":
                break

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
