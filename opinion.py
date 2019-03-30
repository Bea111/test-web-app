from flask import Flask, request, render_template
import requests
app= Flask ("app")
import tweepy
import requests
import json
from tweepy import Cursor


consumer_key = '5xheezAB2vzghReH7Y6g4u0VG'
consumer_secret= 'j2PhwIVReofVP5yB2Sn9DDEXzG4nqD1r1215q3JVk1sHrnScbj'
access_token = '1104794487027630082-9aF4UXhR75ewvVgLLNZUnPnilK9RTB'
access_token_secret= 'rNVpa809y6ZsoGLrOWCw1DvdJliI4fNJk6aDThGIUoLky'


auth  =  tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token (access_token,  access_token_secret)
twitter_api  =  tweepy.API(auth)

#Search tweets
search_words = "#mindfulness"
date_since = "2018-11-16"

#Collect tweets


tweets = tweepy.Cursor(twitter_api.search,
    q = search_words,
    lang = "en").items(10)
#Iterate on tweets
def tweet_main():
    response=[]
    for tweet in tweets:
        response.append(tweet.user.name + ':' + tweet.text)
    return response 





'''
#Collect a list of tweets
[tweet.text for tweet in tweets]

#cfg tweets
cfg_tweets  =  twitter_api.search(
q  =   "CodeFirstGirls") #Twitter handle you want to search by )

for tweet in cfg_tweets:
    print (tweet.user.name  +   ': '   +  tweet.text  + '\n')
'''
