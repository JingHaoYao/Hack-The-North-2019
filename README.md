# Hack-The-North-2019
Hack The North Repository
We created a video game review search tool that offers more accurate recommendations for games by utilizing Microsoft Azure Cognitive Services Text Analytics tool to gain deeper insight.

Our data was collected from meta-critic, see notebooks/metacritic_critic_reviews.csv
Genres were mapped on by cross referencing data from notebooks/steam-store-games/steam.csv
Data is currently saved to a local database that is generated upon running the script

## Usage
Run run_app.py in terminal/command_prompt.

## Parameters
-c .csv file used to update database
<br>
-a api-key for microsoft azure cognitive services
<br>
-e endpoint for microsoft azure cognitive sercices
<br>
-k search terms, seperated by commans without spaces, to find games according to search phrases. Currently only supports 1 word phrases
