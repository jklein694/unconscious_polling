import csv

import tweepy

import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('result.csv', 'a')

# Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q="#obamacare",
                           lang="en").items():
    with open('data.csv', 'w') as f:
        f.write('Author,Date,Text')
        writer = csv.writer(f)
        writer.writerow([tweet.author.screen_name, tweet.created_at, tweet.text])
        print(tweet.author.screen_name, tweet.created_at, tweet.text)
    # Write a row to the CSV file. I use encode UTF-8
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    # print(tweet.created_at, tweet.text)
    # csvFile.close()  # class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         print(status.author.screen_name, status.created_at, status.text)
#         with open('file.csv', 'w') as f:
#             f.write('Author,Date,Text')
#             writer = csv.writer(f)
#             writer.writerow([status.author.screen_name, status.created_at, status.text])
#
#     def on_error(self, status_code):
#         print(sys.stderr, 'Encountered error with status code:', status_code)
#         return True  # Don't kill the stream
#
#     def on_timeout(self):
#         print(sys.stderr, 'Timeout...')
#         return True  # Don't kill the stream
#
#
# twitter_stream = MyStreamListener()
#
# stream = tweepy.Stream(auth=api.auth, listener=twitter_stream)
#
# print(stream.filter(track=['#obamacare']))

# search_text = "#obamacare"
# search_number = 2
# search_result = api.search(search_text, rpp=search_number)
# for i in search_result:
#     print(i.text)
