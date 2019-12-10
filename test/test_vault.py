import unittest
from password_manager.vault import Vault


service1, username1, password1 = 'Example Service', 'test_username', 'SECretPassWORDD!'
service2, username2, password2 = 'service 2', 'another-username', 'asesomepassword'


class TestSQLite3(unittest.TestCase):
    def setUp(self):
        self.vault = Vault(':memory:')
        self.vault.nuke_table()

    def test_1insert_entry(self):
        self.vault.add_entry(service1, username1, password1)
        entries = self.vault.get_entries()
        self.assertEqual(tuple, type(entries))      # Always tuple if only one entry, else list

    def test_2no_duplicate_inserts(self):
        self.vault.add_entry(service1, username1, password1)
        entries = self.vault.get_entries()
        self.assertEqual(tuple, type(entries))

    def test_3delete_entry(self):
        self.vault.delete_entry(service1)
        entries = self.vault.get_entries()
        self.assertEqual(0, len(entries))

    def test_4_nuke_table(self):
        self.vault.nuke_table()
        self.assertEqual(0, len(self.vault.get_entries()))


if __name__ == '__main__':
    unittest.main()
