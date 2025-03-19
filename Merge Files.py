import pandas as pd
import numpy as np

# Cleaning up batter data and merging 
gamechanger_bt_df = pd.read_csv('files/HTO + Gamechanger Data/GameChanger Dataset - GameChanger Batters.csv')
hto_bt_df = pd.read_csv('files/HTO + Gamechanger Data/HTO Regular Season Dataset - HTO Batters-Regular-Season.csv')
gamechanger_df = gamechanger_bt_df[gamechanger_bt_df["PA"] != 0]
gamechanger_df = gamechanger_df.assign(Name=gamechanger_df["First"] + " " + gamechanger_df["Last"])
column_to_move = gamechanger_df.pop("Name")
gamechanger_df.insert(1, "Name", column_to_move)
gamechanger_df = gamechanger_df.drop(columns=["Last", "First"])
gamechanger_hto_merge = hto_bt_df.merge(gamechanger_df, left_on=["Name", "No"], right_on=["Name", "Number"])
gamechanger_hto_merge = gamechanger_hto_merge.drop(columns=[i for i in gamechanger_hto_merge.columns if i[-1] == "y"])

# Saving the converted batting data to a CSV file
gamechanger_hto_merge.to_csv('files/HTO + Gamechanger Data/HTO GameChanger Batter Merge - Regular Season - merge_batter_df_updated.csv')

# Cleaning up pitcher data and merging
gamechanger_pt_df = pd.read_csv('files/HTO + Gamechanger Data/GameChanger Dataset - GameChanger Pitchers.csv')
hto_pt_df = pd.read_csv('files/HTO + Gamechanger Data/HTO Regular Season Dataset - HTO Pitchers-Regular Season.csv')
gamechanger_pt_df = gamechanger_pt_df[gamechanger_pt_df["IP"] > 0]
gamechanger_pt_df = gamechanger_pt_df.assign(Name=gamechanger_pt_df["First"] + " " + gamechanger_pt_df["Last"])
column_to_move = gamechanger_pt_df.pop("Name")
gamechanger_pt_df.insert(1, "Name", column_to_move)
gamechanger_pt_df = gamechanger_pt_df.drop(columns=["Last", "First"])
gamechanger_hto_pt_merge = hto_pt_df.merge(gamechanger_pt_df, left_on=["Name", "No"], right_on=["Name", "Number"])
gamechanger_hto_pt_merge = gamechanger_hto_pt_merge.drop(columns=[i for i in gamechanger_hto_pt_merge.columns if i[-1] == "y"])
gamechanger_hto_pt_merge.to_csv('files/HTO + Gamechanger Data/HTO_GameChanger_Pitcher_Merge.csv')

# Function to convert innings to a consistent format
def innings_converter(ip):
    if int(str(ip).split('.')[-1]) == 1:
        return int(str(ip).split('.')[0]) + 0.333
    elif int(str(ip).split('.')[-1]) == 2:
        return int(str(ip).split('.')[0]) + 0.667
    else:
        return ip

merge_pitcher_df = pd.read_csv("files/HTO + Gamechanger Data/HTO_GameChanger_Pitcher_Merge.csv")
merge_pitcher_df = merge_pitcher_df.assign(IP=merge_pitcher_df["INN"].apply(innings_converter)).drop(columns=["INN"])
merge_pitcher_df.insert(4, "IP", merge_pitcher_df.pop("IP"))
merge_pitcher_df = merge_pitcher_df.drop(merge_pitcher_df.columns[0], axis=1)

# Saving the converted pitching data to a CSV file
merge_pitcher_df.to_csv('files/HTO + Gamechanger Data/HTO GameChanger Pitcher Merge - Regular Season - merge_pitcher_df_updated.csv')
