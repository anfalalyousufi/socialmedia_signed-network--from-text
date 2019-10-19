#!/usr/bin/env python
# coding: utf-8

# ## Signed network from text
# #### Twitter is a gold mine of data. Unlike other social platforms, almost every user’s tweets are completely public and pullable. This is a huge plus if you’re trying to get a large amount of data to run analytics on. Twitter data is also pretty specific. Twitter’s API allows you to do complex queries like pulling every tweet about a certain topic within the last twenty minutes, or pull a certain user’s non-retweeted tweets.
# 

# #### Importing 

# In[ ]:


import requests
import json
import final
import tweepy
import os


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

from textblob import TextBlob

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import re #regular expression 

#credentianls
import anfalkeys


# In[6]:


r = final.authenticate("anfalkey.json")
ENDPOINT_URL = "https://stream.twitter.com/1.1/statuses/sample.json"


# ##### Collecting tweets 

# In[ ]:


resp = r.get(ENDPOINT_URL, stream=True)

output_file = open("Tweets.json", "w")

MAX_TWEETS = 1000000
counter = 0
for line in resp:
    if counter > MAX_TWEETS:
        output_file.close()
        break
    if counter % 100:
        print("Saved {} tweets.".format(counter + 1))
    print(line, file=output_file)
    counter += 1


# In[ ]:





# In[ ]:





# #### Selecting using search 

# In[ ]:


#auth = tweepy.0AuthHandler(consumer_key, consumer_secret) #two arguments
#auth.set_access_token(access_token, access_token_secret)

auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
    return auth
    
    

api = tweepy.API(auth)

#collect tweets with certain key words
public_tweets = api.search('Trump')

#print all out "increment every value in a list"
for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)
    print("")


# In[ ]:


class TwitterClient(object):
    def__init__(self,query, retweets_only = False, with_sentiment = False):
        r = final.authenticate("anfalkey.json")
        self.query = query
        self.retweets_only = retweets_only
        self.with_sentiment = with_sentiment 
        self.api = tweetpy.APU (self.auth)
        self.tweet_count_max = 1000 #prevent rate limiting
    except:
        print ("error: authentication failed")
        
def set_query(self, query=''):
        self.query = query
def set_retweet_checking(self, retweets_only='false'):
        self.retweets_only = retweets_only
def set_with_sentiment(self, with_sentiment='false'):
        self.with_sentiment = with_sentiment
def clean_tweet(self, tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#geting sentiments for each tweet between -1 to 1
def get_tweet_sentiment(self, tweet):
    analysis = TextBlob(self.clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    
#get tweets
def get_tweets(self):
    tweets = []
    
     try:
        recd_tweets = self.api.search(q=self.query,
                                          count=self.tweet_count_max)
        if not recd_tweets:
            pass
        for tweet in recd_tweets:
            parsed_tweet = {}

        parsed_tweet['text'] = tweet.text
        parsed_tweet['user'] = tweet.user.screen_name
                
        if self.with_sentiment == 1:
             parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
        else:
             parsed_tweet['sentiment'] = 'unavailable'

        if tweet.retweet_count > 0 and self.retweets_only == 1:
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
        elif not self.retweets_only:
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
        return tweets
    
    except tweety.TweetError as e:
        print ("error:" + str(e))


# In[ ]:


from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from textblob import TextBlob
 
import anfalkey.json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re


class TwitterAnalysis():
    def__init__(self,twitter_user=None, query, retweets_only = False, with_sentiment = False):
       
        self.query = query
        self.retweets_only = retweets_only
        self.with_sentiment = with_sentiment 
        self.api = tweetpy.APU (self.auth)
        self.tweet_count_max = 1000 #prevent rate limiting
    except:
        print ("error: authentication failed")
        
def set_query(self, query=''):
        self.query = query
def set_retweet_checking(self, retweets_only='false'):
        self.retweets_only = retweets_only
def set_with_sentiment(self, with_sentiment='false'):
        self.with_sentiment = with_sentiment
def clean_tweet(self, tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#geting sentiments for each tweet between -1 to 1
def get_tweet_sentiment(self, tweet):
    analysis = TextBlob(self.clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    
#get tweets
def get_tweets(self):
    tweets = []
    
     try:
        recd_tweets = self.api.search(q=self.query,
                                          count=self.tweet_count_max)
        if not recd_tweets:
            pass
        for tweet in recd_tweets:
            parsed_tweet = {}

        parsed_tweet['text'] = tweet.text
        parsed_tweet['user'] = tweet.user.screen_name
                
        if self.with_sentiment == 1:
             parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
        else:
             parsed_tweet['sentiment'] = 'unavailable'

        if tweet.retweet_count > 0 and self.retweets_only == 1:
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
        elif not self.retweets_only:
            if parsed_tweet not in tweets:
                tweets.append(parsed_tweet)
        return tweets
    
    except tweety.TweetError as e:
        print ("error:" + str(e))


# #### Streaming Live Tweets

# In[ ]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#credentianls
import anfalkeys

#class for streaming & processing live tweets
class TwitterStreamer ():
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
         listener = StdOutListener()
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)

        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        #stream.filter(track=['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders'])
        stream.filter(track=hash_tag_list)


#basic listener class that just prints recieved tweets to stdout       
class StdOutListener(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, data): #overwriting & print the status methos 
        print(status)
        
if __name__ == "__main__":
    hash_tag_list = ["donald trump", "Kylie jenner"]
    fetched_tweets_filename = "hashtag_tweets.json"
    
    #twitter streaming object
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    
   


# #### Cursor and Pagination
# 

# In[9]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

#credentianls
import anfalkeys

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        #stream.filter(track=['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders'])
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
if __name__ == "__main__":
    hash_tag_list = ["Donald Trump", "Kylie jenner"]
    fetched_tweets_filename = "hashtag_tweets.json"
    
    
    twitter_client = TwitterClient('pycon')
    print(twitter_client.get_user_timeline_tweets(1))
    #twitter streaming object
   # twitter_streamer = TwitterStreamer()
   # twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    
   


# #### Analyzing Tweet Data
# ##### take some tweets & analyze them using numpy and pandas

# In[21]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

import numpy as np
import pandas as pd

#credentianls
import anfalkeys

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        #stream.filter(track=['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders'])
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
#class responsible for analyzing and categorizing tweets
class TweetAnalyzer():
    def tweets_to_data_frame(self, tweets):
        #we are creating a list and looping thro' every single tweet and extract text
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets']) #given by panda 
        
        #store id - numpy array - lopp through tweets to get id
        df['Id'] = np.array([tweet.id for tweet in tweets])
        df['Len'] = np.array([len(tweet.text) for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Source'] = np.array([tweet.source for tweet in tweets])
        df['Num of Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Num of Retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return df
        
if __name__ == "__main__":
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()
    
    tweets = api.user_timeline(screen_name = "KylieJenner", count=10)
    
    #print (dir(tweets[0]))
    #print(tweets[0].id)
    #print (tweets[0].retweet_count)
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    print(df.head(10))
   


# #### Visualizing Tweet Data

# In[35]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#credentianls
import anfalkeys

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        #stream.filter(track=['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders'])
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
#class responsible for analyzing and categorizing tweets
class TweetAnalyzer():
    def tweets_to_data_frame(self, tweets):
        #we are creating a list and looping thro' every single tweet and extract text
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets']) #given by panda 
        
        #store id - numpy array - lopp through tweets to get id
        df['ID'] = np.array([tweet.id for tweet in tweets])
        df['Len'] = np.array([len(tweet.text) for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Source'] = np.array([tweet.source for tweet in tweets])
        df['Num of Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Num of Retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return df
        
if __name__ == "__main__":
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    
    api = twitter_client.get_twitter_client_api()
    
    tweets = api.user_timeline(screen_name = "KylieJenner", count=200)

    df = tweet_analyzer.tweets_to_data_frame(tweets)
    
    #avg length of all the tweets
    print(np.mean(df['Len']))
    
    #tweets with most likes
    print(np.max(df['Num of Likes']))
    
    #number of retweets
    print (np.max(df['Num of Retweets']))
    
    #time series to show the number of likes based on a given day
    #time_likes = pd.Series(data = df['Num of Likes'].values, index = df['Date'])
    #time_likes.plot(figsize =(16,4), color = 'pink')
    
    #time_retweets = pd.Series(data = df['Num of Retweets'].values, index = df['Date'])
    #time_likes.plot(figsize =(16,4), color = 'blue')
    #plt.show()
    
    time_likes = pd.Series(data = df['Num of Likes'].values, index = df['Date'])
    time_likes.plot(figsize =(16,4), label ="Num of Likes", legend=True)
    
    time_retweets = pd.Series(data = df['Num of Retweets'].values, index = df['Date'])
    time_retweets.plot(figsize =(16,4), label ="Num of Retweets", legend=True)
    
    plt.show()


# #### Sentiment Analysis
# ##### whether the tweet is -ve, +ve or neutral using textblob (has build in semtiment analyzer)

# In[69]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

from textblob import TextBlob

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import re #regular expression 

#credentianls
import anfalkeys

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
#class responsible for analyzing and categorizing tweets
class TweetAnalyzer():
       
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
  
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['ID'] = np.array([tweet.id for tweet in tweets])
        df['Len'] = np.array([len(tweet.text) for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Source'] = np.array([tweet.source for tweet in tweets])
        df['Num of Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Num of Retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df
    
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

    tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
    
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    print(df.head(10))
    
 
    
    #tweets = api.user_timeline(screen_name="KylieJenner", count=200)
    #df = tweet_analyzer.tweets_to_data_frame(tweets)
    #df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    #print(df.head(10))
        


# #### Hashtag

# In[29]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

from textblob import TextBlob

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import re #regular expression 

#credentianls
import anfalkeys

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
#class responsible for analyzing and categorizing tweets
class TweetAnalyzer():
       
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
  
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['ID'] = np.array([tweet.id for tweet in tweets])
        df['Len'] = np.array([len(tweet.text) for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Source'] = np.array([tweet.source for tweet in tweets])
        df['Num of Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Num of Retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df
    
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

   # tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
   # for tweets in tweepy.Cursor (api.search, q="#maleficent", count = 200, lang='en').items():
   #     print (tweet.created_at, tweet.text)
    tweets= api.search(q='#maleficent', count=20)
    #tweets = api.search['statuses']

    #for tweet in tweets:
          #print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
    
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    print(df.head(10))


# In[2]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

from textblob import TextBlob

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import re #regular expression 

#credentianls
import anfalkeys

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
#class responsible for analyzing and categorizing tweets
class TweetAnalyzer():
       
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
  
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['ID'] = np.array([tweet.id for tweet in tweets])
        df['Len'] = np.array([len(tweet.text) for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Source'] = np.array([tweet.source for tweet in tweets])
        df['Num of Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Num of Retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df
    
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()

   # tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
   # for tweets in tweepy.Cursor (api.search, q="#maleficent", count = 200, lang='en').items():
   #     print (tweet.created_at, tweet.text)
    tweets= api.search(q='#maleficent', count=20, lang='en')
    #tweets = api.search['statuses']

    #for tweet in tweets:
          #print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
    
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    print(df.head(10))


# #### Sample search "tweets.json"

# In[ ]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API
from tweepy import Cursor 

from textblob import TextBlob

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import re #regular expression

#credentianls
import anfalkeys
import json

#twitter client
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = Authentication().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client

    #funtion to get tweets
    def get_user_timeline_tweets(self, num_tweets):
        tweets =[]
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    
    def get_friend_list(self, num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends, id= self.twitter_user).items(num_friends):
            friend_list.append(friends)
        return friend_list
    
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets =[]
        for tweet in Cursor (self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    
#authentication class
class Authentication():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(anfalkeys.CONSUMER_KEY, anfalkeys.CONSUMER_SECRET)
        auth.set_access_token(anfalkeys.TOKEN_KEY, anfalkeys.TOKEN_SECRET)
        return auth
    
    
#class for streaming & processing live tweets
class TwitterStreamer ():
    def __init__(self):
        self.twitter_authenticator = Authentication()
    
    
    def stream_tweets (self, fetched_tweets_filename, hash_tag_list):
        # This handles twittter authentication & the connection to the twitter streaming api
        listener = TwitterLis(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
    
        #focused on some keywords of hashtags
        stream.filter(track=hash_tag_list)


#printing tweets & writing it into a file
class TwitterLis(StreamListener):
    def __init__ (self,fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    def on_data(self,data): #take data that is streamed in from the stream listener so the one that's listening for tweets
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data: %s" %str(e))
        return True
 
    
    def on_error(self, status): #overwriting & print the status methos 
        if status == 420:
            return False #kill connection -return false data method in case rate limit occurs
        print(status)
        
#class responsible for analyzing and categorizing tweets
class TweetAnalyzer():
       
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
  
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['ID'] = np.array([tweet.id for tweet in tweets])
        df['Len'] = np.array([len(tweet.text) for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Source'] = np.array([tweet.source for tweet in tweets])
        df['Num of Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Num of Retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df
    
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()
###reading from json

#prompt the user for a file to import
filter = "tweets"
filename = rs.OpenFileName("Open JSON File", filter)

#Read JSON data into the datastore variable
if filename:
    with open(tweets, 'r') as f:
        datastore = json.load(f)

    
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    df['Sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    print(df.head(10))


# In[ ]:




