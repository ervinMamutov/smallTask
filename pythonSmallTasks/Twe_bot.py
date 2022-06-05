import tweepy

# Authenticate to Twitter

auth = tweepy.QAuthHandler('CONSUMER_KEY', 'CONSUMER_SECRET')
auth.set_access_token('ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')

# Create API object
api.update_status('Hello Tweepy')



