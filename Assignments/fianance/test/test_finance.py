import unittest
from dao.finance_repository_impl import FinanceRepositoryImpl
from entity.user import User
from entity.expense import Expense

class TestFinanceSystem(unittest.TestCase):
    def setUp(self):
        self.repo = FinanceRepositoryImpl()

    def test_create_user(self):
        u = User(username="testuser", password="pass", email="test@example.com")
        self.assertTrue(self.repo.create_user(u))

    def test_create_expense(self):
        e = Expense(user_id=1, amount=99.99, category_id=1, date="2025-04-30", description="Test")
        self.assertTrue(self.repo.create_expense(e))

if __name__ == "__main__":
    unittest.main()
