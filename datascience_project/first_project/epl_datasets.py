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

# print oldest player in any team

'''
liverpool_df = df[df['team'].str.strip().str.lower() == 'liverpool'][df['season'] == 2425][['player', 'team', 'age_']]
print(liverpool_df[liverpool_df['age_'] == liverpool_df['age_'].max()][['player', 'team', 'age_']])
'''
# print any oldest player from any team on any season
def get_oldest_player(df, team, season):
    filtered_df = df[
        (df['team'].str.strip().str.lower() == team.lower()) &
        (df['season'] == season) 
    ][['player', 'team', 'age_', 'league']]

    print(filtered_df[filtered_df['age_'] == filtered_df['age_'].max()])

# print oldest player in every league by season
def get_oldest_player_by_season(df, season) :
    df_2425 = df[df['season'] == season]
    df_league = df_2425.loc[df_2425.groupby('league')['age_'].idxmax(), ['team', 'player', 'age_', 'league']]
    print(df_league)

get_oldest_player_by_season(df, 2425)

print(get_oldest_player(df, 'Liverpool', 2425))
'''
result = df_2425.loc[df_2425.groupby('team')['age_'].idxmax(), ['team', 'player', 'age_', 'league']]
print(result)
'''