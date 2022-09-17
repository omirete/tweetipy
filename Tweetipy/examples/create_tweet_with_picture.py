from dotenv import load_dotenv
from os import getenv
from Tweetipy import Tweetipy
from Tweetipy.types import Media

load_dotenv()

ttpy = Tweetipy(
    oauth_consumer_key=getenv('TWITTER_API_KEY'),
    oauth_consumer_secret=getenv('TWITTER_API_KEY_SECRET')
)

with open('dog.jpeg', 'rb') as pic:
    uploaded_media = ttpy.media.upload(
        media_bytes=pic.read(),
        media_type="image/jpeg")

print(
    ttpy.tweets.write(text="On my way to the club 🐶",
    media=Media([uploaded_media.media_id_string]))
)