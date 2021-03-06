import tweepy
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import logging
import os

logger = logging.getLogger()

fnt1 = ImageFont.truetype('Ubuntu-BI.ttf', 35)
fnt2 = ImageFont.truetype('Ubuntu-BI.ttf', 25)

def startBot():
    # Authenticate to Twitter
    consumer_key =  os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    
    return api

def createProgressBar():   	 
    with Image.open("../images/white.jpg") as img:
        w, h = img.size
        draw = ImageDraw.Draw(img)

        # Main bar
        shape = [w - 200, h - 400, 200, 400]
        draw.rectangle(shape, fill="#f4f4f4", outline="red", width=1)
        draw.text((200, 690), "0%", font=fnt1, fill='black')
        draw.text((w - 200, 690), "100%", font=fnt1, fill='black')

        # Details
        shape = [330, 230, 200, 200]
        draw.rectangle(shape, fill="#9ad5a9", width=1)
        draw.text((350, 200), "Población cordobesa con al menos una dosis", font=fnt2, fill='black')

        shape = [330, 280, 200, 250]
        draw.rectangle(shape, fill="#19d849", width=1)
        draw.text((350, 250), "Población cordobesa con pauta completa", font=fnt2, fill='black')

        img.save("../images/bar.jpg")

def getDateScructure(date):
    dt = datetime.strptime(date, '%d/%m/%Y')

    return dt

def updateProgressBar(percentage1D, percentagePautaCompleta, date):
    with Image.open("../images/bar.jpg") as img:
        draw = ImageDraw.Draw(img)
        w, h = img.size

        # "Al menos 1D" progress
        shape = [(w - 200) * percentage1D/100, h - 400, 200, 400]
        draw.rectangle(shape, fill="#9ad5a9", outline="red", width=1)
        draw.text(((w - 200) * percentage1D/100, 350), f"{percentage1D}%", font=fnt1, fill='black')

        # "Pauta completa" progress
        shape = [(w - 200) * percentagePautaCompleta/100, h - 400, 200, 400]
        draw.rectangle(shape, fill="#19d849", outline="red", width=1)
        draw.text(((w - 200) * percentagePautaCompleta/100, 350), f"{percentagePautaCompleta}%", font=fnt1, fill='black')

        # Date
        draw.text((w/2.3, 750), f"{date}", font=fnt1, fill='black')

        dt = getDateScructure(date)

        img.save(f"../images/{dt.year}-{dt.month}-{dt.day}.jpg")

def isNewData(api, print_info):
    # Get last tweet
    last_tweet = api.user_timeline(screen_name=api.me().screen_name, 
                                   # 200 is the maximum allowed count
                                   count=1,
                                   include_rts = False,
                                   # Necessary to keep full_text 
                                   # otherwise only the first 140 words are extracted
                                   tweet_mode = 'extended')

    last_tweet = [tweet.full_text for tweet in last_tweet]

    # Compare date of last tweet and new tweet
    old_date = last_tweet[0].split()[7]
    new_date = print_info.split()[7]

    if old_date == new_date:
        return False
    return True
