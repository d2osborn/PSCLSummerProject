import pandas as pd
import numpy as np

# Function to change specific team names
def team_changer(*teams):
    for team in teams:
        team = team.strip()
        if team == "Dragons":
            return "Green Dragons"
        elif team == "LumberJacks":
            return "Lumberjacks"
        else:
            return team

# Function to remove numbers from player names
def number_removal(*players):
    for player in players:
        player = player.split(" ")
        player = [i for i in player if i.isalpha() == True]
        return " ".join(player).strip()

# Function to remove null pitches and keep specific pitch types
def remove_null_pitches(*pitches):
    for pitch in pitches:
        if pitch in ["Changeup", "Curveball", "Cutter", "Four Seam Fastball", "Slider", "Two Seam Fastball"]:
            return pitch
        else:
            return "null"

# Read the flightscope data and drop columns with empty/irrelevant data
flightscope_df = pd.read_csv('')
flightscope_df = flightscope_df.drop(columns=[i for i in flightscope_df if "Col" in i])
flightscope_df = flightscope_df.drop(columns=["PA of Inning", "Pitch of PA", "Notes", "Supervisor"])
flightscope_df = flightscope_df.rename(columns={"Home Team.1": "Away Team"})
flightscope_df = flightscope_df.dropna(subset=["Pitcher Team", "Batter Team", "Pitch Speed [mph]"])

# Update pitcher teams using the team_changer function
pitcher_updated_team = flightscope_df.apply(lambda row: team_changer(row["Pitcher Team"]), axis=1)
flightscope_df["Pitcher_Team"] = pitcher_updated_team
flightscope_df.insert(6, "Pitcher_Team", flightscope_df.pop("Pitcher_Team"))
flightscope_df = flightscope_df.drop(columns=["Pitcher Team"])
flightscope_df = flightscope_df.rename(columns={"Pitcher_Team": "Pitcher Team"})

# Update batter teams using the team_changer function
updated_team = flightscope_df.apply(lambda row: team_changer(row["Batter Team"]), axis=1)
flightscope_df["Batter_Team"] = updated_team
flightscope_df.insert(10, "Batter_Team", flightscope_df.pop("Batter_Team"))
flightscope_df = flightscope_df.drop(columns=["Batter Team"])
flightscope_df = flightscope_df.rename(columns={"Batter_Team": "Batter Team"})

# Remove numbers from pitcher names using the number_removal function
updated_pitchers = flightscope_df.apply(lambda row: number_removal(row["Pitcher"]), axis=1)
flightscope_df["Pitcherss"] = updated_pitchers
flightscope_df = flightscope_df.drop(columns=["Pitcher"])
flightscope_df.insert(3, "Pitcherss", flightscope_df.pop("Pitcherss"))
flightscope_df = flightscope_df.rename(columns={"Pitcherss": "Pitcher"})

# Remove numbers from batter names using the number_removal function
updated_batters = flightscope_df.apply(lambda row: number_removal(row["Batter"]), axis=1)
flightscope_df["Batterss"] = updated_batters
flightscope_df = flightscope_df.drop(columns=["Batter"])
flightscope_df.insert(7, "Batterss", flightscope_df.pop("Batterss"))
flightscope_df = flightscope_df.rename(columns={"Batterss": "Batter"})

# Change empty pitches to "null" using the remove_null_pitches function
updated_pitches = flightscope_df.apply(lambda row: remove_null_pitches(row["Pitch Type"]), axis=1)
flightscope_df["Pitch_Type"] = updated_pitches
flightscope_df = flightscope_df.drop(columns=["Pitch Type"])
flightscope_df.insert(13, "Pitch_Type", flightscope_df.pop("Pitch_Type"))
flightscope_df = flightscope_df.rename(columns={"Pitch_Type": "Pitch Type"})

# Remove rows with "null" in the "Pitch Type" column
flightscope_df = flightscope_df[flightscope_df.get("Pitch Type") != "null"]

# Remove rows with single-word pitcher and batter names
flightscope_df = flightscope_df[flightscope_df['Pitcher'].str.split().apply(len) > 1]
flightscope_df = flightscope_df[flightscope_df["Batter"].str.split().apply(len) > 1]

# Save the cleaned data to a CSV file
flightscope_df.to_csv('')
