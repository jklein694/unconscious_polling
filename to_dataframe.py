# import pandas as pd
#
#
# import pandas as pd
# import json
# dict1 = {}
# dict2 = {}
# print(json.loads(json.dumps([dict1, dict2])))
#
# counter = 0
# for jsonFile in jsonFiles:
# with open(jsonFile) as f:
#     data = f.read()
#     jsondata = json.loads(data)
#     try:
#         db[args.collection].insert(jsondata)
#         counter += 1
#
# with open('#obamacare/#obamacare_2017-11-14.json') as f:
#    data = json.load(f)
# print(data)
#
# print(pd.DataFrame(data))
#
# # df = pd.read_json('#obamacare_2017-11-14.json', lines=True)
# # print(df.columns)

import json

import pandas as pd

tweet_files = ['#obamacare/#obamacare_2017-11-14.json']
tweets = []
for file in tweet_files:

    with open(file, 'r') as f:
        for line in f.readlines():
            tweets.append(json.loads(line))


def populate_tweet_df(tweets):
    df = pd.DataFrame()

    df['text'] = list(map(lambda tweet: tweet['text'], tweets))

    df['location'] = list(map(lambda tweet: tweet['user']['location'], tweets))

    df['country_code'] = list(map(lambda tweet: tweet['place']['country_code']
    if tweet['place'] != None else '', tweets))

    df['long'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][0]
    if tweet['coordinates'] != None else 'NaN', tweets))

    df['latt'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][1]
    if tweet['coordinates'] != None else 'NaN', tweets))

    return df


df = populate_tweet_df(tweets)

df.to_csv('tweet_data.csv')
