import tweepy 
import csv
import pandas as pd
import auth #AUTH İÇİN GEREKLİ KEY'LER

client = tweepy.Client(auth.BEARER_TOKEN) #TWITTER APIV2 AUTH
list_id = "" #LIST_ID GİR
list_tweets = client.get_list_tweets(id=list_id)

file = open('list_tweets', 'w+', newline ='')
 
with file:   
    write = csv.writer(file)
    write.writerows(list_tweets)


df_new = pd.read_csv('list_tweets.csv')
 
GFG = pd.ExcelWriter('tweet_listesi_excel.xlsx')
df_new.to_excel(GFG, index=False)
 
