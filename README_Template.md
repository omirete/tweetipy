# Tweetipy
A simple type hinted Python client for interacting with Twitter's API.

```
pip -m install tweetipy
```

To use it, setup a developer account under [developer.twitter.com](https://developer.twitter.com/).

After that, create an app from the [developer dashboard](https://developer.twitter.com/en/portal/dashboard) and generate the needed tokens ("API Key and Secret").

Please note that the library does not yet implement the full Twitter API, but rather only some endpoints that are interesting for my projects. Also, although it is already working, please be aware that this library is still in early development phase and thus breaking changes might occur. In other words, don't rely on it for production just yet.

In any case, feel free to use it for your own projects. Do create issues if anything weird pops up. Pull requests and feature requests are welcome!

# Examples

### Posting a tweet
```python
_fill_with_contents_of:examples/create_tweet.py
```

### Posting a tweet with media
```python
_fill_with_contents_of:examples/create_tweet_with_picture.py
```

### Searching tweets
```python
_fill_with_contents_of:examples/search_tweets/simple_search.py
```

### Doing advanced searches - Single condition
```python
_fill_with_contents_of:examples/search_tweets/advanced_search_single_cond.py
```

### Doing advanced searches - Multiple conditions (AND)
```python
_fill_with_contents_of:examples/search_tweets/advanced_search_multiple_cond.py
```

### Doing advanced searches - Multiple conditions (OR)
```python
_fill_with_contents_of:examples/search_tweets/advanced_search_alternative_cond.py
```
