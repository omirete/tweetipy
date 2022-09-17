from dotenv import load_dotenv
from os import getenv
from tweetipy import Tweetipy
from tweetipy.types import Media

load_dotenv()

ttpy = Tweetipy(
    oauth_consumer_key=getenv('TWITTER_API_KEY'),
    oauth_consumer_secret=getenv('TWITTER_API_KEY_SECRET'))

# First upload the media to Twitter.
with open('dog.jpeg', 'rb') as pic:
    uploaded_media = ttpy.media.upload(
        media_bytes=pic.read(),
        media_type="image/jpeg")

# Then post a tweet, adding the media_id as a parameter.
ttpy.tweets.write(
    text="This tweet contains some media.",
    media=Media([uploaded_media.media_id_string]))