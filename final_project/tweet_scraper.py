# -*- coding: utf-8 -*-

import tweepy
import requests
from access import *
import json
import os
from collections import defaultdict
from dotenv import load_dotenv
load_dotenv()


class TwitterBot:
    def __init__(self, tweets_file):
        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            # Return API access:
            self.api = tweepy.API(auth, wait_on_rate_limit=True,
                                  wait_on_rate_limit_notify=True, compression=True)

            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            raise Exception('Error! Failed to get request token, please complete \
                            access file')
        self.tweets_file = tweets_file
        try:
            with open(self.tweets_file) as f:
                self.tweets = json.load(f)
        except FileNotFoundError:
            self.tweets = defaultdict(list)


    def retrieve_tweets(self, user, count=20, include_rts=False):
        try:
            return self.api.user_timeline(screen_name=user, count=count,
                                          include_rts=include_rts)
        except Exception as e:
            raise e


    def print_tweets(self, tweets):
        for i in tweets:
            print(i.text+"\n")


    def search(self, target, since='2019-08-1', until=None, limit=100):
        ''' Collect all the tweets with the keyword
        target
        '''

        cursor = tweepy.Cursor(
            self.api.search,
            q=target,
            since=since,
            until=until,
            lang='es',
            tweet_mode='extended',
            show_user=True)

        seen = set()
        print(f'Recovering {target} tweets')
        for tweet in cursor.items(limit):
            if tweet.full_text not in seen:
                try:
                    favs = tweet.retweeted_status.favorite_count
                    text = tweet.retweeted_status.full_text
                except AttributeError:
                    favs = 0
                    text = tweet.full_text

                self.tweets[target].append({
                                            'created_at': tweet.created_at, 
                                            'tweet': text,
                                            'retweet_count': tweet.retweet_count,
                                            'source': tweet.source,
                                            'favorite_count': favs,
                                            'id': tweet.id,
                                            })
                seen.add(tweet.full_text)
        print(f'{len(seen)} tweets recovereds..')

    def save_tweets(self):
        with open(self.tweets_file, 'w') as f:
            json.dump(self.tweets, f, indent=4, default=str, ensure_ascii=False)

if __name__ == '__main__':
    bot = TwitterBot('tweets.json')
    mentions = ['@alferdez', '@mauriciomacri', '@CFKArgentina', 'Macri', 'Alberto Fernandez', 'CFK']
    for mention in mentions:
        ## Last 5000 tweets for each mention
        bot.search(target=mention, limit=5000)
    bot.save_tweets()
