from dotenv import load_dotenv
from os import getenv
from tweetipy import Tweetipy
from tweetipy.helpers import QueryBuilder

load_dotenv()

ttpy = Tweetipy(
    oauth_consumer_key=getenv('TWITTER_API_KEY'),
    oauth_consumer_secret=getenv('TWITTER_API_KEY_SECRET')
)

t = QueryBuilder()

search_results = ttpy.tweets.search(
    query=t.with_all_keywords(['dogs', 'love']) & t.has.media,
    sort_order='relevancy'
)

print(search_results)
