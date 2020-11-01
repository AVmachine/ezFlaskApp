

def return_dataframe ():

    import os
    import kaggle
    from io import StringIO # For creation of string inputs to be read as '.tsv' by pandas
    import re # For separation of netflix_df.country strings into lists
    import gzip # For extraction of IMDB datasets
    import urllib.request
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib
    import matplotlib.pyplot as plt

    #%matplotlib inline


    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('shivamb/netflix-shows', path=os.getcwd(), unzip=True)

    netflix_df_raw = pd.read_csv('netflix_titles.csv')
    netflix_df = netflix_df_raw.copy()
    netflix_df

    #Download IMDB files from official repository
    urllib.request.urlretrieve('https://datasets.imdbws.com/title.ratings.tsv.gz', 'title.ratings.tsv.gz');
    urllib.request.urlretrieve('https://datasets.imdbws.com/title.basics.tsv.gz', 'title.basics.tsv.gz');

    #extract files as text
    with gzip.open('title.ratings.tsv.gz', 'rt', encoding='utf8') as reader:
        ratings_contents = reader.read()

    with gzip.open('title.basics.tsv.gz', 'rt', encoding='utf8') as reader:
        basics_contents = reader.read()

    # Create text strings to be loaded into panda.read_csv as a tab separated file
    ratings_data = StringIO(ratings_contents)
    basics_data = StringIO(basics_contents)

    # Create pandas dataframe from tab separated file for ratings
    imdb_ratings_df_raw = pd.read_csv(ratings_data, sep='\t')
    imdb_ratings_df = imdb_ratings_df_raw.copy()

    # Create pandas dataframe from tab separated file for titles
    imdb_titles_df_raw = pd.read_csv(basics_data, sep='\t')
    imdb_titles_df = imdb_titles_df_raw.copy()

    # inner join btw the two IMDB dataframes
    imdb_combo_df = pd.merge(imdb_titles_df, imdb_ratings_df, on='tconst')
    imdb_combo_df

    #Join the two datasets with the intention of having only the titles on netflix remain, but include their information from IMDB
    final_df_raw = pd.merge(netflix_df, imdb_combo_df, left_on='title', right_on='primaryTitle')
    final_df = final_df_raw.copy()

    final_df.country = final_df.country.fillna('Unknown')
    final_df.director = final_df.director.fillna('Unknown')
    final_df.date_added = final_df.date_added.fillna('January 1, 2001')

    final_df = final_df.groupby('cast').agg({'title':'max', 'type':'max', 'director':'max', 'country':'max', 'date_added':'max', 'description':'max', 'averageRating':'mean', 'numVotes':'sum'}).reset_index()


    return final_df.iloc[1:101]
