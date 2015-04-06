# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:45:09 2015

@author: Maharsh

This program prints out the tweet, the time the tweet was created, the username, location, and the language of the tweet 

"""
import json
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'INSERT CONSUMER KEY HERE'
csecret = 'INSERT CONSUMER SECRET HERE'
atoken = 'INSERT AUTHORIZATION TOKEN HERE'
asecret = 'INSERR AUTHORIZATION SECRET HERE'


class listener(StreamListener):
    
    def on_data(self, data):
    	#Replace all lines[that have the comment REPLACE with print(data) if you want all the tweet information 
        data = json.loads(data)							#REPLACE
        print("TWEET: " + data['text'])						#REPLACE
        print("CREATED AT: " + data['created_at'])				#REPLACE
        print("Username: " + data['user']['screen_name'])			#REPLACE
        print("Location: " + data['user']['location'])				#REPLACE
        print("Language: " + data['user']['lang'])				#REPLACE
        print("\n\n")
        
        return True
    
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[input("SEARCH QUERY: ")])

