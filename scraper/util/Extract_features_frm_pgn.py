import pandas as pd
import os

class Extract_features():
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(os.path.join(path, 'games.csv' ) )

    def get_features(self):

        # The additional features we can extract from the pgn are :-
        #'Event', 'Site', 'Start_Date', 'End_Date', 'Start_time', 'End_time', 'Round', 'Result',
        # 'Tournament', 'ECO', 'First_Move', 'Second_Move', 'Third_Move', 'Fourth_Move'

        feature_names = ['Event', 'Site', 'Start_Date', 'End_Date', 'Start_Time',
                        'End_Time', 'Eco', 'EcoName', 'Round', 'Result', 'Game_Type']
        feature_positions = [0, 1, 2, -6, -7, -5, -15, -14, 3, 6, 7]

        # Takes in the name you want to give the feature, and the position of the feature in
        # the pgn.split('\n') and creates the feature with feature name in the dataframe

        for feature_name, position in zip(feature_names, feature_positions):
            self.df[feature_name] = self.df['pgn'].apply(
                lambda x: x.split('\n')[position].split('"')[1])

        # The ECO Codes is a classification system for the chess openings moves.<br>
        # There are five main categories, "A" to "E", corresponding to the five volumes of the
        # earlier editions, each of which is further subdivided into 100 subcategories, for a
        # total of 500 codes. The term "ECO" is often used as a shorthand for this coding system.
        # We can also extract the Eco_Name using the EcoName feature we extracted from the pgn

        self.df['Eco_Name'] = self.df.EcoName.apply(lambda x: x.split('/')[-1])

        # Upon seeing both the pgn of the 1st row and the 2nd row I noticed a difference,
        # There are two types of game here, played in a Tournament, and played as a regular match
        # Using this Information we can create another feature :- Is_Tournament

        self.df['Is_tournament'] = self.df['Game_Type'].apply(lambda x: 'tournament' in x)
        self.df.to_csv(os.path.join(self.path, 'games.csv'))