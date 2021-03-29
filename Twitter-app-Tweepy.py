from sys import getprofile
import tweepy
import pandas as pd
from tweepy.api import API
from tweepy.models import Status
from OAuthTwitter import *
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_Token,access_TokenSecret)
api = tweepy.API (auth,wait_on_rate_limit=True)


def extract_place(row):
    if row['Place Info']:
        return row['Place Info'].full_name
    else:
        return "No Registra - Latam"

busqueda = 'Huawei'
max_tweets = 100

tweets = tweepy.Cursor(api.search,q=busqueda,lang='es').items(max_tweets)

tweets_list = [[tweet.text, tweet.created_at, tweet.user.screen_name, tweet.place, tweet.retweet_count, tweet.lang] for tweet in tweets]
 
tweets_df = pd.DataFrame(tweets_list,columns=['Tweet Text', 'Tweet Datetime',  'Twitter @ Name', 'Place Info', 'Retweets', 'Language'])
 


tweets_df['Place Info'] = tweets_df.apply(extract_place,axis=1)
tweets_df.to_csv('csv1 - Twitter.csv',index= False, sep=";")
print ((tweets_df))

'''

userName = "Nike"

userGet = api.get_user(userName)
location = userGet.location 

print(location)

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        
        print (status.text)
        if status.coordinates:
            print ('coords:', status.coordinates)
        if status.place:
            print ('place:', status.place.full_name)
        

        return True

    on_event = on_status

    def on_error(self, status):
        print (status)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['zapatillas','pesos'],languages=['es'])

   '''