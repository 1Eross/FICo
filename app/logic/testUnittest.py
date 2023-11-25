import unittest
from logic.User import UserAccount
class TestUser (unittest.TestCase):
    def TestRegistration (self):
        self.assertEqual(UserAccount.Registration)

