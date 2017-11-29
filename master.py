import new_names as get_from_twitter
import get_data as clean_data
import preprocess as prep

# get_from_twitter.run_search(['@cnn', '@foxnews', '@breitbartnews', '@nytimes', '@huffpost',
#                              '@bbc', '@msnbc', '@wsj', '@forbes', '#fakenews', '#liar', '#notmypresident',
#                              '#trump', '#hillary', '#maga', '#Imwithher'])
data = clean_data.run_cleaner()
data = prep.run_preprocess(data)
