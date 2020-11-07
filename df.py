import pandas as pd

def test_df():
    dataframe = pd.read_csv('test_df.csv')
    return dataframe

def getDataForChartJs(dataframe):

    dictionaryOfCountriesVsRatings = {}
    dictionaryOfCountriesAndCount = {}
    for i in range(100):
        if(dataframe.iloc[i].values[5] in dictionaryOfCountriesVsRatings):
            dictionaryOfCountriesVsRatings[dataframe.iloc[i].values[5]] += dataframe.iloc[i].values[8]
            dictionaryOfCountriesAndCount[dataframe.iloc[i].values[5]] += 1
        else:
            dictionaryOfCountriesVsRatings[dataframe.iloc[i].values[5]] = dataframe.iloc[i].values[8]
            dictionaryOfCountriesAndCount[dataframe.iloc[i].values[5]] = 1

    for key in dictionaryOfCountriesAndCount:
        dictionaryOfCountriesVsRatings[key] = dictionaryOfCountriesVsRatings[key]/dictionaryOfCountriesAndCount[key]



    print(dictionaryOfCountriesVsRatings)
    print(dictionaryOfCountriesAndCount)




