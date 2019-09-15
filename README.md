# Video Game Recommender
Hack The North Repository
We created a video game review search tool that offers more accurate recommendations for games by utilizing Microsoft Azure Cognitive Services Text Analytics tool to gain deeper insight.

Our data was collected from meta-critic, see notebooks/metacritic_critic_reviews.csv

See our devpost: https://devpost.com/software/video-game-recommender-ai
<br>
Genres were mapped on by cross referencing data from notebooks/steam-store-games/steam.csv
<br>
Data is currently saved to a local database that is generated upon running the script

## Usage
Run run_app.py in terminal/command_prompt.
<br>
Example: in directory - $python src/run_app.py -c [csv_file_path] -a [api-key] -e [endpoint] -k [search terms]

## Parameters
-c .csv file used to update database (optional)
<br>
-a api-key for microsoft azure cognitive services
<br>
-e endpoint for microsoft azure cognitive services
<br>
-k search terms, seperated by commans without spaces, to find games according to search phrases. Currently only supports 1 word phrases (optional)
