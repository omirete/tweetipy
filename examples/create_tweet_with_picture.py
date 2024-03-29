from tweetipy import Tweetipy
from tweetipy.types import MediaToUpload

ttpy = Tweetipy(
    'YOUR_TWITTER_API_KEY',
    'YOUR_TWITTER_API_KEY_SECRET')

# First upload the media to Twitter.
with open('dog.jpeg', 'rb') as pic:
    uploaded_media = ttpy.media.upload(
        media_bytes=pic.read(),
        media_type="image/jpeg")

# Then post a tweet, adding the media_id as a parameter.
ttpy.tweets.write(
    "This tweet contains some media.",
    media=MediaToUpload([uploaded_media.media_id_string]))
