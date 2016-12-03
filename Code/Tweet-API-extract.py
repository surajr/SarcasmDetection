import io
import sys
from textblob import TextBlob
import tweepy
import re

   
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'

access_token='access_token'
access_token_secret='access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Step2 - Call the API
api = tweepy.API(auth)
output = ''    

with io.open("Fracking-Sarcasm-using-Neural-Network.txt") as fopen:
    file_content = fopen.read().splitlines()
    
for i in range(0,len(file_content)-1):
    try:
        temp = re.split(r'\t+',file_content[i])
        tweet, label = temp[0], temp[1]
        status = api.get_status(tweet)
        output += status.text + " " + label + "\n"
    except:
        continue
outputfile = io.open('tweetcontent.txt','w',encoding='utf8')
outputfile.write(output)
outputfile.close() 

   

