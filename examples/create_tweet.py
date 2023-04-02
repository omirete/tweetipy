from tweetipy import Tweetipy

# Initialize client
ttpy = Tweetipy(
    'YOUR_TWITTER_API_KEY',
    'YOUR_TWITTER_API_KEY_SECRET')

# Post tweet to Twitter
tweet = ttpy.tweets.write("I'm using Twitter API!")

# See the uploaded tweet! :)
print(tweet)
