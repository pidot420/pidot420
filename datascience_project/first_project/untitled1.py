# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:44:08 2026

@author: pidot
"""
'''
import pandas as pd
df = pd.read_csv("C:/Users//pidot//Documents//datascience_project//first_project//Top5_League_Players_2017to2024_dataset.csv")
df.head()
'''
import pandas as pd
# Source - https://stackoverflow.com/a/66657167
# Posted by dallonsi, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-20, License - CC BY-SA 4.0

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("C:/Users/pidot/Documents/datascience_project/first_project/Top5_League_Players_2017to2024_dataset.csv", sep=";", dtype={"team" : str})

##print(df[df['team']=='Arsenal'])
liverpool_df = df[df['team'].str.strip().str.lower() == 'liverpool'][df['season'] == 2425][['player', 'team', 'age_']]
print(liverpool_df[liverpool_df['age_'] == liverpool_df['age_'].max()][['player', 'team', 'age_']])
