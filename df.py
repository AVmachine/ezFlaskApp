import pandas as pd


def test_df():
    dataframe = pd.read_csv('final_df.csv')
    df = dataframe.sort_values('numVotes', ascending=False).reset_index()
    df = df.drop('index', axis=1)
    return df

