import unittest
import sys
sys.path.append("C:/Users/user/Documents/GitHub/FICo")
from app.logic.User import UserAccount
class TestUser (unittest.TestCase):
    def test_Registration (self):
        self.assertEqual(UserAccount.Registration("Biba", "89098959772", "maremyanov05@mail.ru", "12345678", "87654321"), True)
        self.assertEqual(UserAccount.Registration("Biba", "89098959772", "maremyanov05@mail.ru", "12345678", "87654321"), False)
        #self.assertEqual(UserAccount.Registration("",), True)
        
if __name__ == '__main__':
    unittest.main()
