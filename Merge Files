import pandas as pd
import numpy as np

# Reading batting data from GameChanger and HTO
gamechanger_bt_df = pd.read_csv('')
hto_bt_df = pd.read_csv('')

# Filtering out rows where Plate Appearances (PA) is zero
gamechanger_df = gamechanger_bt_df[gamechanger_bt_df["PA"] != 0]

# Creating a "Name" column by combining "First" and "Last" columns
gamechanger_df = gamechanger_df.assign(Name=gamechanger_df["First"] + " " + gamechanger_df["Last"])

# Moving "Name" column to the second position
column_to_move = gamechanger_df.pop("Name")
gamechanger_df.insert(1, "Name", column_to_move)

# Dropping unnecessary columns ("Last", "First")
gamechanger_df = gamechanger_df.drop(columns=["Last", "First"])

# Merging GameChanger batting data with HTO batting data using "Name" and "Number" as keys
gamechanger_hto_merge = hto_bt_df.merge(gamechanger_df, left_on=["Name", "No"], right_on=["Name", "Number"])

# Dropping columns ending with 'y'
gamechanger_hto_merge = gamechanger_hto_merge.drop(columns=[i for i in gamechanger_hto_merge.columns if i[-1] == "y"])

# Saving the merged batting data to a CSV file
gamechanger_hto_merge.to_csv('')

# Reading pitching data from GameChanger and HTO
gamechanger_pt_df = pd.read_csv('')
hto_pt_df = pd.read_csv('')

# Filtering out rows where Innings Pitched (IP) is not greater than zero
gamechanger_pt_df = gamechanger_pt_df[gamechanger_pt_df["IP"] > 0]

# Creating a "Name" column by combining "First" and "Last" columns
gamechanger_pt_df = gamechanger_pt_df.assign(Name=gamechanger_pt_df["First"] + " " + gamechanger_pt_df["Last"])

# Moving "Name" column to the second position
column_to_move = gamechanger_pt_df.pop("Name")
gamechanger_pt_df.insert(1, "Name", column_to_move)

# Dropping unnecessary columns ("Last", "First")
gamechanger_pt_df = gamechanger_pt_df.drop(columns=["Last", "First"])

# Merging GameChanger pitching data with HTO pitching data using "Name" and "Number" as keys
gamechanger_hto_pt_merge = hto_pt_df.merge(gamechanger_pt_df, left_on=["Name", "No"], right_on=["Name", "Number"])

# Dropping columns ending with 'y'
gamechanger_hto_pt_merge = gamechanger_hto_pt_merge.drop(columns=[i for i in gamechanger_hto_pt_merge.columns if i[-1] == "y"])

# Saving the merged pitching data to a CSV file
gamechanger_hto_pt_merge.to_csv('')

# Function to convert innings to a consistent format
def innings_converter(ip):
    if int(str(ip).split('.')[-1]) == 1:
        return int(str(ip).split('.')[0]) + 0.333
    elif int(str(ip).split('.')[-1]) == 2:
        return int(str(ip).split('.')[0]) + 0.667
    else:
        return ip

# Reading merged pitching data
merge_pitcher_df = pd.read_csv("")

# Applying the innings converter function to convert 'INN' column and dropping the original 'INN' column
merge_pitcher_df = merge_pitcher_df.assign(IP=merge_pitcher_df["INN"].apply(innings_converter)).drop(columns=["INN"])

# Moving "IP" column to the fourth position
merge_pitcher_df.insert(4, "IP", merge_pitcher_df.pop("IP"))

# Dropping the first column
merge_pitcher_df = merge_pitcher_df.drop(merge_pitcher_df.columns[0], axis=1)

# Saving the converted pitching data to a CSV file
merge_pitcher_df.to_csv('')
