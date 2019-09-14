import os
import sqlite3

class SQliteDB:
    def __init__(self):
        #
        # Path to sqlite database under home directory
        #
        self.sqlite_path = os.getenv("HOME") + "/sqlite.db"

        #
        # Table creation SQL command
        #
        self.create_table = (
            "CREATE TABLE IF NOT EXISTS TEXT_ANALYTICS_RESULTS ("
            #
            # TODO: Figure table schema for storing filtered entries
            #
            ")"
        )

        #
        # Connecting to sqlite database
        #
        self.conn = sqlite3.connect(self.sqlite_path)
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()

        #
        # Create table
        #
        self.cursor.execute(self.create_table)
        self.conn.commit()

    def delete_all_entries(self):
        #
        # Delete all entries from table SQL command
        #
        delete_entries = "DELETE FROM TEXT_ANALYTICS_RESULTS"

        self.cursor.execute(delete_entries)
        self.conn.commit()

    def insert_into_db(self, *args):
        #
        # Insert SQL command
        #
        insert_entries = (
            "INSERT INTO TEXT_ANALYTICS_RESULTS ("
            #
            # TODO: Figure table schema for storing filtered entries
            #
            ") "
            "values ()"
        )

        params = (
            #
            # TODO: table schema
            #
        )

        self.cursor.execute(insert_entries, params)

    def select_from_db(self, *args):
        select_command = (
            "SELECT * FROM TEXT_ANALYTICS_RESULTS"
        )

        self.cursor.execute(select_command)
        self.conn.commit()
