import os
import requests
from pprint import pprint
from db import SQliteDB
from pandas import DataFrame
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import csv
import json

class TextAnalytics:
    def init(self, _csv, _api_key, _endpoint):
        self.csv_path = _csv
        self.api_key = _api_key
        self.endpoint = _endpoint
        self.db = SQliteDB()

        #
        # Azure text analytic endpoint urls
        #
        self.sentiment_endpoint = self.endpoint + "text/analytics/v2.1/sentiment"
        self.keyphrase_endpoint = self.endpoint + "text/analytics/v2.1/keyPhrases"

        self.client = TextAnalyticsClient(endpoint=self.endpoint)

    def parse_csv(self):
        rows = []
        with open(self.csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                rows.append(row)

        return rows

    def send_to_text_analytics(self, data_frame):
        for index, row in data_frame.iterrows():
            documents = [
                {
                    "id": row["game_name"],
                    "language" : "en",
                    "text": row["review_text"]
                }
            ]

            json_formatted = json.dumps(documents)

            response_sentiment = client.sentiment(documents=documents)
            response_key_phrases = client.key_phrase(documents=documents)

            #
            # Extract sentiment
            #
            extracted_sentiment_response = json.load(response_sentiment)
            extracted_sentiment = int(extracted_sentiment_response["documents"]["score"] * 100)

            for document in response_key_phrases.documents:
                for phrase in document.key_phrases:
                    self.db.insert_into_db(document.id, extracted_sentiment, phrase)

            self.db.insert_into_db()
