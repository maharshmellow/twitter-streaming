# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:45:09 2015

@author: Maharsh
"""
import json
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = ''
csecret = ''
atoken = ''
asecret = ''


class listener(StreamListener):
    
    def on_data(self, data):
        data = json.loads(data)
        print("TWEET: " + data['text'])
        print("CREATED AT: " + data['created_at'])
        print("Username: " + data['user']['screen_name'])
        print("Location: " + data['user']['location'])
        print("Language: " + data['user']['lang'])
        #user - followers_count, friends_count, 
        print("\n\n")
        
        return True
    
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[input("SEARCH QUERY: ")])

