from dao.ifinance_repository import IFinanceRepository
from util.db_conn_util import DBConnUtil
from exception.user_not_found_exception import UserNotFoundException
from exception.expense_not_found_excpetion import ExpenseNotFoundException

class FinanceRepositoryImpl(IFinanceRepository):
    def create_user(self, user):
        conn = DBConnUtil.get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Users (username, password, email) VALUES (?, ?, ?)",
                    (user.get_username(), user.get_password(), user.get_email()))
        conn.commit()
        return True

    def create_expense(self, e):
        conn = DBConnUtil.get_connection()
        cur = conn.cursor()
        cur.execute("""INSERT INTO Expenses (user_id, amount, category_id, date, description)
                       VALUES (?, ?, ?, ?, ?)""",
                    (e.get_user_id(), e.get_amount(), e.get_category_id(), e.get_date(), e.get_description()))
        conn.commit()
        return True

    def delete_user(self, user_id):
        conn = DBConnUtil.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Users WHERE user_id=?", (user_id,))
        if cur.rowcount == 0:
            raise UserNotFoundException()
        conn.commit()
        return True

    def delete_expense(self, eid):
        conn = DBConnUtil.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Expenses WHERE expense_id=?", (eid,))
        if cur.rowcount == 0:
            raise ExpenseNotFoundException()
        conn.commit()
        return True

    def get_all_expenses(self, uid):
        conn = DBConnUtil.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Expenses WHERE user_id=?", (uid,))
        return cur.fetchall()

    def update_expense(self, uid, e):
        conn = DBConnUtil.get_connection()
        cur = conn.cursor()
        cur.execute("""UPDATE Expenses SET amount=?, category_id=?, date=?, description=?
                       WHERE expense_id=? AND user_id=?""",
                    (e.get_amount(), e.get_category_id(), e.get_date(), e.get_description(),
                     e.get_expense_id(), uid))
        if cur.rowcount == 0:
            raise ExpenseNotFoundException()
        conn.commit()
        return True
