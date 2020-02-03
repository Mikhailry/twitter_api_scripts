"""
The following script uses the Twitter search API for “your search query” and print to the screen a list of distinct hashtags appearing in first 100 results the API returns and the number of times each hashtag appears.
"""

# importing libraries
import tweepy
import json
import os
from itertools import groupby

# show the working directory
os.getcwd()

# authentication credentials (Stored here for your convinience)
auth = tweepy.OAuthHandler('consumer key', 'consumer secret')
auth.set_access_token('access token', 'access token secret')

# verify credentials
try:
    api.verify_credentials()
    print('Authentication successful')
except:
    print('Authentication failed')

# twitter api authentication
api = tweepy.API(auth)

# get the @user user id
uid = api.get_user('twitter_user_name')


# create empty list to store hashtags
ht=[]
# search for #Seattle
tweets = tweepy.Cursor(api.search, q='#Seattle', lang='en').items(100)
# extract hashtags from api output
ent = [tweet.entities['hashtags'] for tweet in tweets]
ht= [t['text'].lower() for item in ent for t in item]

# count the hashtags frequency
results = {value: len(list(freq)) for value, freq in groupby(sorted(ht))}
print(results)
