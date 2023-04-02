from tweetipy import Tweetipy
from tweetipy.helpers import QueryBuilder

# Initialize the client
ttpy = Tweetipy(
    'YOUR_TWITTER_API_KEY',
    'YOUR_TWITTER_API_KEY_SECRET')

# The query builder is your friend :)
t = QueryBuilder()

# Define the search criteria using the query builder.
search_results = ttpy.tweets.search(
    query=t.from_user('Randogs8'),
    sort_order='recency'
)

# See results 🤩
for tweet in search_results:
    print(tweet)
