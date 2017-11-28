# Gets all the data from data folder and returns just the tweet and the hashtag
import os
import re

import pandas as pd


def run_cleaner():
    # List files in data directory
    file_paths = os.listdir('data')

    df = pd.DataFrame()

    for file_path in file_paths:
        # Read in jsons and add them to one data frame
        file_data = pd.read_json('data/{}'.format(file_path), lines=True)

        df = pd.concat([df, file_data])

    # List comprehension to pull only hashtags and tweets from large json file
    data = pd.DataFrame.from_records([[[z['text'] for z in x['hashtags']], y]
                                      for x, y in zip(df.entities, df.text) if type(x) == dict],
                                     columns=['hashtag', 'text'])

    # Create False column for null values
    data['to_drop'] = [True if len(x) > 0 else False for x in data.hashtag]

    # Drop null values
    data = data[data.to_drop]

    data = data.drop('to_drop', 1)

    # Remove hashtags from tweets and all special characters
    data.text = [' '.join(re.sub("(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x).split()) for x in data.text]

    # For loop to separate rows fro tweets with multiple hashtags
    updated_list = []

    for x, y in data.values:
        for j in x:
            updated_list.append(([j, y]))

    # Create DataFrame and export to csv
    data = pd.DataFrame(updated_list, columns=['hashtag', 'tweet'])

    data.to_csv('clean_data.csv')

    return data
