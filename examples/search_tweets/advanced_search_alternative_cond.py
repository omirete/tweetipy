from tweetipy import Tweetipy
from tweetipy.helpers import QueryBuilder

# Initialize the client
ttpy = Tweetipy(
    'YOUR_TWITTER_API_KEY',
    'YOUR_TWITTER_API_KEY_SECRET')

# The query builder is your friend :)
t = QueryBuilder()

# Use the pipe operator (|) to define alternative criteria.
# The query builder will do some background work for you so this works as
# expected. 😎
search_results = ttpy.tweets.search(
    query=t.from_user('Randogs8') | t.from_user('cooldogfacts'),
    sort_order='recency'
)

# See the results 🤩
for tweet in search_results:
    print(tweet)
