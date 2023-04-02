from tweetipy import Tweetipy

# Initialize the client
ttpy = Tweetipy(
    'YOUR_TWITTER_API_KEY',
    'YOUR_TWITTER_API_KEY_SECRET')

# Treat the 'query' argument as you would a search box.
search_results = ttpy.tweets.search(query='space separated keywords')


# See results 🤩
for tweet in search_results:
    print(tweet)
