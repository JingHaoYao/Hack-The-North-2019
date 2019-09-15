import os
import sqlite3
import nltk
import pandas as pd
from suggestions import Suggestion
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
import math

class SQliteDB:
    def __init__(self):
        #
        # Path to sqlite database under home directory
        #
        self.sqlite_path = "sqlite.db"

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
            "REVIEWER_ID, "
            "RATING INT NOT NULL"
            ")"
        )

        self.create_view_command = (
            "ALTER VIEW RESULTS AS SELECT LOWER(KEYWORD) AS KEYWORD, "
            "GAME_NAME, COUNT(*) AS KEYWORD_OCCURENCES, "
            "AVG(SENTIMENT) AS AVG_SENTIMENT "
            "FROM TEXT_ANALYTICS_RESULTS GROUP BY KEYWORD, GAME_NAME"
        )

        self.create_view_command_2 = (
            "CREATE VIEW IF NOT EXISTS FILTERED_GAME_SET AS SELECT GAME_NAME, MAX(GENRE), AVG(RATING) FROM (SELECT MAX(GAME_NAME), MAX(GENRE), MAX(RATING) "
            "FROM GAME_DATA_SET GROUP BY REVIEWER_ID) GROUP BY GAME_NAME"
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

    def insert_into_db_2(self, game_name, genre, reviewer, rating):
        #
        # Insert SQL command
        #

        insert_entries = (
            "INSERT INTO GAME_DATA_SET ("
            "GAME_NAME, "
            "GENRE, "
            "REVIEWER_ID, "
            "RATING"
            ") "
            "values (?, ?, ?, ?)"
        )

        params = (
            game_name,
            genre,
            reviewer,
            rating
        )

        self.cursor.execute(insert_entries, params)
        self.conn.commit()

    def generate_suggestions_features(self, key_phrases)
        #
        # Get all game names
        #
        query_games = (
            "SELECT GAME_NAME FROM FILTERED_GAME_SET"
        )

        self.cursor.execute(query_games)
        self.conn.commit()

        game_list = self.cursor.fetchall()

        #
        # The score of the maximum scoring suggestion
        #
        max_suggestion_score = 0
        
        # 
        # The maximum scoring suggestion
        #
        max_suggestion = None

        for game_name in game_list:
            select_game = (
                "SELECT * FROM RESULTS WHERE GAME_NAME={} AND AVG_SENTIMENT > 50".format(game_name)
            )
            
            selected_data_frame = pd.read_sql_query(select_game, self.conn)

            w2v_model = self.summarize_set(selected_data_frame)

            #
            # Total matching score of the suggestion
            #
            total_score = 0

            #
            # Iterates through the list of entries within the title
            #
            for index, row in selected_data_frame:
                for key_phrase in key_phrases:
                    #
                    # Get list of tuples that are similar to key phrase and their matching score
                    #
                    matches = w2v_model.most_similar(key_phrase)

                    #
                    # Check for the key_phrase itself
                    #
                    if key_phrase == row["KEYWORD"]:
                        totalscore += row["KEYWORD_OCCURENCES"] * 10 + 100

                    for match in matches:
                        #
                        # checks if the review contains a similar word to the keyphrase
                        #
                        if match == row["KEYWORD"]:
                            total_score += 70 * math.tanh((row["KEYWORD_OCCURENCES"] * 10) / 50)

            if total_score > max_suggestion_score:
                #
                # Compare total score to current max suggestion score
                # and set max suggestion to the new max
                #
                max_suggestion_score = total_score
                max_suggestion = Suggestion(game_name, total_score)

        return max_suggestion

    def summarize_set(self, keyword_set):
        standarized_list = []
        lemmatizer = WordNetLemmatizer()
        for index, data in keyword_set.iterrows():
            standarized_keywords = []
            for word in data[0].split():
                if word not in STOPWORDS:
                    word = lemmatizer.lemmatize(word.lower())
                    standarized_keywords.append(word)
            for y in range(data[2]):
                standarized_list.append(standarized_keywords)
        w2v_model = Word2Vec(standarized_list)
        return w2v_model

