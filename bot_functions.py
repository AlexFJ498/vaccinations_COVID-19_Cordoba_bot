import tweepy
from PIL import Image, ImageDraw, ImageFont


def startBot(consumer_key, consumer_secret, access_token, access_token_secret):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    return tweepy.API(auth)

def progressBar():   	 
    with Image.open("image.jpg") as im:
        w, h = 620, 190
        shape = [(40, 40), (w - 10, h - 10)]
        draw = ImageDraw.Draw(im)
        draw.rectangle(shape, fill="green", outline="red", width=1)

        im.save("result.jpg")