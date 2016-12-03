import io
import sys
from textblob import TextBlob
import tweepy
import re

with io.open("Fracking-Sarcasm-using-Neural-Network.txt") as fopen:
    file_content = fopen.read().splitlines()

    
consumer_key= 'SMVEA3MypMkgOeAGjn75N0gHJ'
consumer_secret= 'skaKGnyqPpzGO9PHubYaEVygai6fQB95ZkZQJrFFYaJfXZvI8J'

access_token='715755192994643968-NgdBmvMLFm7QotE1sZezym6daI0WyOD'
access_token_secret='d9B1xOXUzlgNyGa8Zyex09V6sTz4RUS5a4yPVqwCyiNRV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Step2 - Call the API
api = tweepy.API(auth)
output = ''    
    
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
    

   

