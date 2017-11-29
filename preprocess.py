import re

import pandas as pd
from nltk.corpus import stopwords

negative = pd.read_csv('negative-words.csv', sep='\n', header=None)
negative.columns = ['word']


positive = pd.read_csv('positive-words.csv', sep='\n', header=None)
positive.columns = ['word']


sentiment = pd.concat([positive, negative])


def review_to_words(tweets):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and
    # the output is a single string (a preprocessed movie review)
    letters_only = re.sub("[^a-zA-Z]", " ", tweets)
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))
    #
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]

    #
    # 6. Join the words back into one string separated by space,
    # and return the result.
    return (" ".join(meaningful_words))


def count_pos_neg_sent(tweets):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and
    # the output is a single string (a preprocessed movie review)
    letters_only = re.sub("[^a-zA-Z]", " ", tweets)
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()

    neg_words = [w for w in words if w in negative.word.values]

    neg_count = len(neg_words)

    pos_words = [w for w in words if w in positive.word.values]

    pos_count = len(pos_words)
    return pos_count, neg_count


def run_preprocess(data):
    print("Cleaning and parsing the training set for tweets...\n")
    clean_train_tweets = []
    print(data.head())
    num_tweets = len(data.tweet)
    for i in range(0, num_tweets):
        # If the index is evenly divisible by 1000, print a message
        if ((i + 1) % 10000 == 0):
            print("Review %d of %d\n" % (i + 1, num_tweets))

        clean_train_tweets.append(review_to_words(data.tweet[i]))

    print(clean_train_tweets)

    print("Counting positive and negative words in tweets...\n")
    positive_count = []
    negative_count = []
    num_tweets = len(data.tweet)
    for i in range(0, num_tweets):
        # If the index is evenly divisible by 1000, print a message
        if ((i + 1) % 10000 == 0):
            print("Review %d of %d\n" % (i + 1, num_tweets))
        p, n = count_pos_neg_sent(clean_train_tweets[i])
        positive_count.append(p)
        negative_count.append(n)

    sentiment_count = []

    for i in range(len(data.tweet)):
        if positive_count[i] > negative_count[i]:
            sentiment_count.append(1)
        if positive_count[i] < negative_count[i]:
            sentiment_count.append(-1)
        if positive_count[i] == negative_count[i]:
            sentiment_count.append(0)

    data['sentiment'] = sentiment_count

    print(data.head())

    data.to_csv('preprocess_data.csv')

    return data
