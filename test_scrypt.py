import unittest

from flask_scrypt import generate_random_salt, generate_password_hash, check_password_hash

class ScryptTestCase(unittest.TestCase):

    def test_is_string(self):
        salt = generate_random_salt()
        print(type(str(salt))
        self.assertTrue(isinstance(salt, str))

if __name__ == '__main__':
    unittest.main()
