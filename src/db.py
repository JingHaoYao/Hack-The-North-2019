import os
import sqlite3
import nltk

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
<<<<<<< HEAD
=======
            ")"
        )

        self.create_table_2 = (
            "CREATE TABLE IF NOT EXISTS GAME_DATA_SET ("
            "GAME_NAME TEXT NOT NULL, "
            "GENRE TEXT NOT NULL, "
            "RATING INT NOT NULL"
>>>>>>> 38b82efc0e1d96bdff76670ec9f6e2696274e2cc
            ")"
        )

        self.create_table_2 = (
            "CREATE TABLE IF NOT EXISTS GAME_DATA_SET ("
            "GAME_NAME TEXT NOT NULL, "
            "GENRE TEXT NOT NULL, "
            "REVIEWER_ID, "
            "RATING INT NOT NULL"
            ")"
        )

        self.create_view_command = (
            "CREATE VIEW RESULTS AS SELECT KEYWORD, "
            "GAME_NAME, COUNT(*) AS KEYWORD_OCCURENCES, "
            "AVG(SENTIMENT) AS AVG_SENTIMENT "
            "FROM TEXT_ANALYTICS_RESULTS GROUP BY KEYWORD, GAME_NAME"
        )

        self.create_view_command_2 = (
            "CREATE VIEW FILTERED_GAME_SET AS SELECT MAX(GAME_NAME), MAX(GENRE), MAX(RATING) "
            "FROM GAME_DATA_SET GROUP BY REVIEWER_ID"
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
        self.cursor.execute(self.create_table_2)
        self.conn.commit()

        #
        # Create view
        #
        self.cursor.execute(self.create_view_command)
        self.conn.commit()
        self.cursor.execute(self.create_view_command_2)
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
        #
        # TODO: fix this
        #
        insert_entries = (
            "INSERT INTO GAME_DATA_SET ("
            "GAME_NAME, "
            "GENRE, "
            "REVIEWER_ID, "
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

    def generate_suggestions(self, game_name):
        
        self.cursor.execute()
