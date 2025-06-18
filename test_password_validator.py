import unittest
from password_validator import PasswordValidator

class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.validator = PasswordValidator(
            blacklist=['123456', 'password', 'admin', 'Valid@123']
        )

    def test_valid_password(self):
        result, message = self.validator.validate("StrongP@ss1")
        self.assertTrue(result)
        self.assertEqual(message, "Password is valid")

    def test_short_password(self):
        _, message = self.validator.validate("Ab1$")
        self.assertEqual(message, "Password too short")

    def test_missing_uppercase(self):
        _, message = self.validator.validate("weakpass1$")
        self.assertEqual(message, "Missing uppercase letter")

    def test_blacklisted_password(self):
        _, message = self.validator.validate("Valid@123")  # essa senha só falha por estar na blacklist
        self.assertEqual(message, "Password is too common")

    def test_missing_special(self):
        _, message = self.validator.validate("Password1")
        self.assertEqual(message, "Missing special character")

if __name__ == '__main__':
    unittest.main()
