import pandas as pd
import os
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv(os.path.join('data/output', 'games.csv'))
print(df.columns)
df = df.drop(columns=['Unnamed: 0', 'white_username', 'black_username', 'white_id',
       'black_id', 'white_result',
       'black_result',  'fen',
       'pgn', 'Event', 'Site', 'Start_Date', 'End_Date', 'Start_Time',
       'End_Time', 'Round',  'Game_Type', 'Moves', 'Eco', 'EcoName'
       'Eco_Name'])

X = df.drop('Result',axis = 1)
y = df['Result']

print(X.columns)
print(y)

for col in X.columns:
    if X[col].dtype == 'object' or bool:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

result_dict = {'1-0' : 1, '0-1':0, '1/2-1/2':2}
y = [result_dict[v] for v in y]
y = pd.Series(y).values

skf = StratifiedKFold(n_splits = 5)
for trn_, val_ in skf.split(X, y):
        X_train = X.iloc[trn_]
        X_valid = X.iloc[val_]
        y_train = y[trn_]
        y_valid = y[val_]
        clf = LogisticRegression(random_state = 42, solver='liblinear')
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_valid)
        print(f'Validation_Score: {metrics.accuracy_score(predictions, y_valid)}')

with open('data/model/model.pkl', 'wb') as f:
    pickle.dump(clf, f)

