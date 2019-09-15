import os
from dotenv import load_dotenv
import argparse
from textanalytics import TextAnalytics

parser = argparse.ArgumentParser()

load_dotenv()

api_key = os.getenv("API_KEY")
endpoint = os.getenv("ENDPOINT")

def parse_args():
    parser.add_argument(
        "-c",
        "--csv",
        help="csv file with data set"
    )

    parser.add_argument(
        "-a",
        "--api_key",
        default=api_key,
        help="api_key for azure text analytics resource"
    )

    parser.add_argument(
        "-e",
        "--endpoint",
        default=endpoint,
        help="endpoint for azure text analytics resource"
    )

    parser.add_argument(
        "-k"
        "--keyphrases",
        help="keyphrases to search for like games"
    )

    return parser.parse_args()

def main():
    args = parse_args()


    if(args.csv != None):
        text_analytics = TextAnalytics(args.csv, args.api_key, args.endpoint)

        #
        # Gathering parsed data and then sending it over to azure
        #
        data = text_analytics.parse_csv()
        text_analytics.send_to_text_analytics(data)

    if(args.keyphrases != None):
        phrases = args.keyphrases.split(",")
        text_analytics.print_suggestion(phrases)

if __name__ == "__main__":
    main()