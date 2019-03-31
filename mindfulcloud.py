from flask import Flask, render_template
app= Flask ("cloud")
# Start with loading all necessary libraries

@app.route("/cloud")


import tweepy
import json
import pandas as pd
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as mpl
import csv
import matplotlib.pyplot as plt

import operator
from textblob import TextBlob
from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer

consumer_key = '5xheezAB2vzghReH7Y6g4u0VG'
consumer_secret= 'j2PhwIVReofVP5yB2Sn9DDEXzG4nqD1r1215q3JVk1sHrnScbj'
access_token = '1104794487027630082-9aF4UXhR75ewvVgLLNZUnPnilK9RTB'
access_token_secret= 'rNVpa809y6ZsoGLrOWCw1DvdJliI4fNJk6aDThGIUoLky'

auth  =  tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token (access_token,  access_token_secret)
twitter_api  =  tweepy.API(auth)

#Extracting Tweets
results = []
for tweet in tweepy.Cursor (twitter_api.search, q = '#mindfulness', lang = "en").items(5):
    results.append(tweet)

print (type(results))
print (len(results))

# Join all the text from the 1000 tweets
Hashtag_Combined = " ".join(Htag_df['Hashtag'].values.astype(str))

no_millennials = " ".join([word for word in Hashtag_Combined.split()
                                if word != 'mindfulness'
                                and word != 'Mindfulness'
                                and word != 'Relax'
                                and word != 'meditation'

                                ])

Tweet_mask = imread("C:\\Users\\kdudani\\Desktop\\Personal\\Social Media Analytics\\twitter_mask.png", flatten=True)

#Create a Word Cloud
wc = WordCloud(background_color="white", stopwords=STOPWORDS, mask = Tweet_mask)
wc.generate(no_millennials)
plt.imshow(wc)
plt.axis("off")
plt.savefig('C:\\Users\\beatrice\\Desktop\\Python\\my_app\\static\\mindful_Hashtag.jpg', dpi=300)
plt.show()
