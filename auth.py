import requests_oauthlib

access_token = 'xxx'
access_secret = 'xxx'
consumer_key = 'xxx'
consumer_secret = 'xxx'

my_auth = requests_oauthlib.OAuth1(consumer_key,
	consumer_secret,
	access_token,
	access_secret)
 