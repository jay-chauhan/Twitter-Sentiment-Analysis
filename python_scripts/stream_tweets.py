import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import api_keys
import my_listener



print(api_keys.consumer_key,api_keys.consumer_secret)
auth = OAuthHandler(api_keys.consumer_key, api_keys.consumer_secret)
auth.set_access_token(api_keys.access_token, api_keys.access_secret)
api = tweepy.API(auth)
twitter_stream = Stream(auth, my_listener.my_listener())
twitter_stream.filter(track=['star'])
