from dotenv import load_dotenv
from os import getenv
from tweetipy import Tweetipy

load_dotenv()

# Initialize client
ttpy = Tweetipy(
    getenv('YOUR_TWITTER_API_KEY'),
    getenv('YOUR_TWITTER_API_KEY_SECRET')
)

# Post tweet to Twitter
tweet = ttpy.tweets.write("I'm using Twitter API!")

# See the uploaded tweet! :)
print(tweet)
