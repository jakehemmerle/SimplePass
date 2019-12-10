import sqlite3, os
from crypto_engine import CryptoEngine


class Vault:
    """
    This class operates on the 'vault' table of the specified SQLite3 DB.
    """

    def __init__(self, secret, database_location='db.sqlite3.enc'):
        if os.path.isfile(database_location) or database_location is ':test:':
            self.engine = CryptoEngine(secret, database_location)
            self.db = sqlite3.connect(self.engine.decrypted_db_location)
        else:
            self.engine = CryptoEngine(secret)
            self.db = sqlite3.connect(self.engine.decrypted_db_location)
            self.nuke_table()

    def __del__(self):
        self.db.close()

    @staticmethod
    def _selection_to_array(selection):
        """
        Turns sqlite return into an array of tuples, or tuple.
        :param selection: results from self.db.execute(SQL HERE)
        :return: db results
        """
        entries = []
        for entry in selection:
            entries.append(entry)
        return entries[0] if len(entries) == 1 else entries

    def initialize_empty_vault(self):
        try:
            with self.db:
                return self.db.execute('create table vault(\n'
                                       '                        id integer primary key,\n'
                                       '                        service_name text not null,\n'
                                       '                        username     text default NULL,\n'
                                       '                        password     text default NULL\n'
                                       '                        );')
        except Exception as e:
            print('Error creating empty table: ')
            print(e)
            return None

    def get_entries(self):
        with self.db:
            return Vault._selection_to_array(self.db.execute('SELECT service_name, username, password FROM vault'))

    def get_entry(self, service_name):
        with self.db:
            return Vault._selection_to_array(self.db.execute(
                'SELECT service_name, username, password FROM vault WHERE service_name = ?', (service_name,)))

    # def get_id_by_service_name(self, service_name):
    #     with self.db:
    #         return Vault._selection_to_array(self.db.execute('''SELECT * FROM vault WHERE service_name = ?''', service_name))

    def delete_entry(self, service_name):
        with self.db:
            return self.db.execute('DELETE FROM vault WHERE service_name = ?', (service_name,))

    def add_entry(self, service_name, username, password):
        if len(self.get_entry(service_name)) == 0:
            return self.insert(service_name, username, password)
        else:
            # TODO: this should be an update, but it's still very little data
            self.delete_entry(service_name)
            return self.insert(service_name, username, password)

    # def update_password_by_id(self, id, password):
    #     with self.db:
    #         return self.db.execute('''UPDATE vault SET password = ? WHERE id = ?''', (password, id))

    def insert(self, service_name, username, password):
        try:
            with self.db:
                return self.db.execute('INSERT INTO vault(id, service_name, username, password) VALUES(NULL,?,?,?)',
                                       (service_name, username, password))
        except Exception as e:
            print('Record already exists')
            print(e)
            return None

    def nuke_table(self):
        try:
            with self.db:
                self.db.execute('DROP TABLE vault')
        finally:
            return self.initialize_empty_vault()
