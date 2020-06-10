"""
The following scipt uses twitter user timeline API and write @twitter_user_name's most recent 100 tweets to a newline-delimited JSON file.
"""


# importing libraries
import tweepy
import json
import os

# show the working directory
os.getcwd()

# authentication credentials (paste your own credentials)
# to get your twitter api credentials - register your app at https://developer.twitter.com/en
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

# get the @user user id and return 100 items
uid = api.get_user('twitter_user_name')

try:
    with open('result.txt', 'w') as outfile:
        for tweet in tweepy.Cursor(api.user_timeline, user_id=uid.id, exclude_replies=True).items(100):
            # create a dict
            tw_dict = json.dumps({'tw_timestamp': str(tweet.created_at), 'tw_text' : tweet.text, 'tw_user' : tweet.user.screen_name}, separators=(',',':'))
            # dump to a file
            json.dump(tw_dict, outfile)
            # add a new line
            outfile.write('\n')
except tweepy.TweepError:
    time.sleep(10)
