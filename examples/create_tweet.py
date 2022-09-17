from dotenv import load_dotenv
from os import getenv
from Tweetipy import Tweetipy

load_dotenv()

ttpy = Tweetipy(
    oauth_consumer_key=getenv('TWITTER_API_KEY'),
    oauth_consumer_secret=getenv('TWITTER_API_KEY_SECRET')
)

print(ttpy.tweets.write(text="New test"))