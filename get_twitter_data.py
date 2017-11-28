# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# Consume:
CONSUMER_KEY    = ''
CONSUMER_SECRET = ''

# Access:
ACCESS_TOKEN  = ''
ACCESS_SECRET = ''

# # We import our access keys:
# from credentials import *    # This will allow us to use the keys as variables
#
# # API's setup:
# def twitter_setup():
#     """
#     Utility function to setup the Twitter's API
#     with our access keys provided.
#     """
#     # Authentication and access using keys:
#     auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#     auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#
#     # Return API with authentication:
#     api = tweepy.API(auth)
#     return api
#
# # We create an extractor object:
# extractor = twitter_setup()
#
# # We create a tweet list as follows:
# tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200)
# print("Number of tweets extracted: {}.\n".format(len(tweets)))
#
# # We print the most recent 5 tweets:
# print("5 recent tweets:\n")
# for tweet in tweets[:5]:
#     print(tweet.text)
#     print()
#
# # We create a pandas dataframe as follows:
# data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
#
# # We display the first 10 elements of the dataframe:
# display(data.head(10))
#
# # Internal methods of a single tweet object:
# print(dir(tweets[0]))
#
# # We print info from the first tweet:
# print(tweets[0].id)
# print(tweets[0].created_at)
# print(tweets[0].source)
# print(tweets[0].favorite_count)
# print(tweets[0].retweet_count)
# print(tweets[0].geo)
# print(tweets[0].coordinates)
# print(tweets[0].entities)
#
# # We add relevant data:
# data['len']  = np.array([len(tweet.text) for tweet in tweets])
# data['ID']   = np.array([tweet.id for tweet in tweets])
# data['Date'] = np.array([tweet.created_at for tweet in tweets])
# data['Source'] = np.array([tweet.source for tweet in tweets])
# data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
# data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
#
# # We extract the mean of lenghts:
# mean = np.mean(data['len'])
#
# print("The lenght's average in tweets: {}".format(mean))
#
