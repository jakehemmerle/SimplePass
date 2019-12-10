import unittest
from password_manager.crypto_engine import CryptoEngine
from password_manager.vault import Vault


test_db = '../data/test_db.sqlite3.enc'


class TestCryptoEngine(unittest.TestCase):
    def test_hash_password_is_deterministic(self):
        engine = CryptoEngine('password')
        hash1 = engine._hash_secret('password')
        hash2 = engine._hash_secret('password')
        print('Hash: ', hash1)

        self.assertEqual(hash1, hash2)

    # def test_gcm_encryption_decryption(self):
    #     engine = CryptoEngine('password')
    #     super_secret_message = b'ok boomer'
    #     ciphertext, tag = engine._get_ciphertext_and_tag(super_secret_message)
    #     print('Message: ', super_secret_message)
    #     print('Ciphertext: ', ciphertext)
    #     plaintext = engine._get_plaintext(ciphertext, tag)
    #     print('Decrypted: ', plaintext)
    #
    #     self.assertEqual(super_secret_message, plaintext)

    def test_vault(self):
        vault = Vault('password', ':test:')
        vault.add_entry('TestArgon2', 'username2', 'password')
        print(vault.get_entries())

        del vault

        vault2 = Vault('password', 'test.db.enc')
        vault2.add_entry('Test1', 'username', 'password3')
        print(vault2.get_entries())


if __name__ == '__main__':
    unittest.main()
