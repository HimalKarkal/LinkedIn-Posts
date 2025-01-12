"""
This script requests a json file from the Australian Open website and extracts player data from it.
Particularly, it extracts each player's name, country, rank, career titles, and career prize money for both men's and women's singles.
"""

# Importing necessary libraries
import requests
import pandas as pd

# URLs for both events
menSingles_url = "https://prod-scores-api.ausopen.com/event/251300/draws"
womenSingles_url = "https://prod-scores-api.ausopen.com/event/251308/draws"

men_dict = requests.get(menSingles_url).json()
women_dict = requests.get(womenSingles_url).json()

# Creating a dataframe to store the data
df = pd.DataFrame(
    columns=[
        "PlayerId",
        "Name",
        "Gender",
        "Country",
        "Rank",
        "CareerTitles",
        "CareerPrizeMoney",
    ]
)

# Extracting player data

# Men's singles
for player in men_dict["players"]:
    Player_Id = player["player_id"]
    Name = player["full_name"]
    Gender = "Male"
    Country = player["nationality"]["name"]
    Rank = int(player["rankings"][0]["ranking"])
    CareerTitles = int(player["career_titles"])
    CareerPrizeMoney = int(player["career_prize_money"])

    data_list = [Player_Id, Name, Gender, Country, Rank, CareerTitles, CareerPrizeMoney]

    df.loc[len(df)] = data_list

# Women's singles
for player in women_dict["players"]:
    Player_Id = player["player_id"]
    Name = player["full_name"]
    Gender = "Female"
    Country = player["nationality"]["name"]
    Rank = int(player["rankings"][0]["ranking"])
    CareerTitles = int(player["career_titles"])
    CareerPrizeMoney = int(player["career_prize_money"])

    data_list = [Player_Id, Name, Gender, Country, Rank, CareerTitles, CareerPrizeMoney]

    df.loc[len(df)] = data_list

# Displaying the first few rows of the dataframe
print(df.head())

# Displaying information about the dataframe
print(df.info())

# Saving the dataframe to a CSV file
df.to_csv("AO_PlayerData.csv", index=False)
