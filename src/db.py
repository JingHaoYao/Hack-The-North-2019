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
            "GAME_NAME TEXT NOT NULL, "
            "SENTIMENT INT NOT NULL, "
            "KEYWORD TEXT NOT NULL"
            ")"
        )

        self.create_table_2 = (
            "CREATE TABLE IF NOT EXISTS GAME_DATA_SET ("
            "GAME_NAME TEXT NOT NULL, "
            "GENRE TEXT NOT NULL, "
            "RATING INT NOT NULL"
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

    def insert_into_db(self, game_name, sentiment, keyword):
        #
        # Insert SQL command
        #
        insert_entries = (
            "INSERT INTO TEXT_ANALYTICS_RESULTS ("
            "GAME_NAME, "
            "SENTIMENT, "
            "KEYWORD"
            ") "
            "values (?, ?, ?)"
        )

        params = (
            game_name,
            sentiment,
            keyword
        )

        self.cursor.execute(insert_entries, params)
        self.conn.commit()

    def insert_into_db_2(self, game_name, genre, rating):
        #
        # Insert SQL command
        #
        insert_entries = (
            "INSERT INTO TEXT_ANALYTICS_RESULTS ("
            "GAME_NAME, "
            "GENRE, "
            "RATING"
            ") "
            "values (?, ?, ?)"
        )

        params = (
            game_name,
            genre,
            rating
        )

        self.cursor.execute(insert_entries, params)
        self.conn.commit()

    def select_from_db(self, *args):
        select_command = (
            "SELECT * FROM TEXT_ANALYTICS_RESULTS"
        )

        self.cursor.execute(select_command)
        self.conn.commit()
