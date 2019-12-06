import unittest
from argon2 import PasswordHasher


class Argon2(unittest.TestCase):
    def test_hash_password(self):
        kdf = PasswordHasher()
        password = 'secretpassword!!'

        hash = kdf.hash(password)

        print('Password: ', password)
        print('Hash: ', hash)

        self.assertTrue(kdf.verify(hash, password))


if __name__ == '__main__':
    unittest.main()
