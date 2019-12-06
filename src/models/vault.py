import sqlite3


def selection_to_array(selection):
    entries = []
    for entry in selection:
        entries.append(entry)
    return entries


class Vault:
    """
    This class operates on the 'vault' table of the specified SQLite3 DB.
    """

    def __init__(self, database_location='../data/db_decrypted.sqlite3'):
        self.db = sqlite3.connect(database_location)

    def __del__(self):
        self.db.close()

    def initialize_empty_vault(self):
        try:
            with self.db:
                return self.db.execute('''create table vault(
                        id int constraint vault_pk primary key,
                        service_name text not null,
                        username     text default NULL,
                        password     text default NULL
                        );''')
        except sqlite3.Error:
            print('Error creating empty table: ')
            return None

    def select_all(self):
        with self.db:
            return selection_to_array(self.db.execute('''SELECT * FROM vault'''))

    def select_entry_by_service_name(self, service_name):
        with self.db:
            return selection_to_array(self.db.execute('''SELECT username, password FROM vault WHERE service_name = ?''', service_name))

    def get_id_by_service_name(self, service_name):
        with self.db:
            return selection_to_array(self.db.execute('''SELECT * FROM vault WHERE service_name = ?''', service_name))

    def delete_entry(self, id):
        with self.db:
            return self.db.execute('''DELETE FROM vault WHERE id = ?''', id)

    def update_password_by_id(self, id, password):
        with self.db:
            return self.db.execute('''UPDATE vault SET password = ? WHERE id = ?''', (password, id))

    def insert(self, service_name, username, password):
        try:
            with self.db:
                return self.db.execute('''INSERT INTO vault(service_name, username, password) VALUES(?,?,?)''',
                                       (service_name, username, password))
        except sqlite3.Error:
            print('Record already exists')
            return None
