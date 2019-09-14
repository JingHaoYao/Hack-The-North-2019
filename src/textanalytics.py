import os
import requests
from pprint import pprint
from db import SQliteDB
import csv

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

    def parse_csv(self):
        rows = []
        with open(self.csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                rows.append(row)

        return rows

    def send_to_text_analytics(self, rows):
        for row in rows:
            #
            # TODO: Implement azure api
            #
            
            #
            # TODO: Write results into db
            #
            self.db.insert_into_db()
