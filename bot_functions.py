import tweepy

def startBot(consumer_key, consumer_secret, access_token, access_token_secret):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    return tweepy.API(auth)