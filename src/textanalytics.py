import os
import requests
from pprint import pprint
from db import SQliteDB
from pandas import DataFrame
import pandas as pd
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import csv
import json

class TextAnalytics:
    def __init__(self, _csv, _api_key, _endpoint):
        self.csv_path = _csv
        self.api_key = _api_key
        self.endpoint = _endpoint
        self.db = SQliteDB()

        #
        # Azure text analytic endpoint urls
        #
        self.sentiment_endpoint = self.endpoint + "text/analytics/v2.1/sentiment"
        self.keyphrase_endpoint = self.endpoint + "text/analytics/v2.1/keyPhrases"


        self.client = TextAnalyticsClient(endpoint=self.endpoint, credentials=CognitiveServicesCredentials(self.api_key))

    def parse_csv(self):
        dataframe = pd.read_csv(self.csv_path)
        return dataframe

    def send_to_text_analytics(self, data_frame):
        for index, row in data_frame.iterrows():
            print(row["game"], row["genre"], row["reviewer_id"], row["overall_score"])
            self.db.insert_into_db_2(row["game"], row["genre"], row["reviewer_id"], row["overall_score"])

            documents = [
                {
                    "id": row["game"],
                    "language" : "en",
                    "text": row["review"]
                }
            ]

            json_formatted = json.dumps(documents)

            response_sentiment = self.client.sentiment(documents=documents)
            response_key_phrases = self.client.key_phrases(documents=documents)

            #
            # Extract sentiment
            #
            extracted_sentiment = int(response_sentiment.documents[0].score * 100)
            # extracted_sentiment = int(extracted_sentiment_response["documents"]["score"] * 100)

            for document in response_key_phrases.documents:
                for phrase in document.key_phrases:
                    print(document.id, extracted_sentiment, phrase)
                    self.db.insert_into_db(document.id, extracted_sentiment, phrase)
