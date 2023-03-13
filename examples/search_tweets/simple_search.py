from dotenv import load_dotenv
from os import getenv
from tweetipy import Tweetipy

load_dotenv()

ttpy = Tweetipy(
    oauth_consumer_key=getenv('TWITTER_API_KEY'),
    oauth_consumer_secret=getenv('TWITTER_API_KEY_SECRET')
)

search_results = ttpy.tweets.search(query='space separated keywords')

print(search_results)
