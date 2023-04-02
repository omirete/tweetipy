from tweetipy import Tweetipy
from tweetipy.helpers import QueryBuilder

# Initialize the client
ttpy = Tweetipy(
    'YOUR_TWITTER_API_KEY',
    'YOUR_TWITTER_API_KEY_SECRET')

# The query builder is your friend :)
t = QueryBuilder()

# Use the 'and' operator (&) to define alternative criteria.
# The query builder will do some background work for you so this works as
# expected. 😎
search_results = ttpy.tweets.search(
    query=t.with_all_keywords(['dogs', 'love']) & t.has.media,
    sort_order='relevancy'
)

# See the results 🤩
for tweet in search_results:
    print(tweet)
