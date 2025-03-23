import tweepy
from modules.client import tweeter


def main():

    client = tweeter()

    test_tweet = "Return the Slab!!!"
    client.create_tweet(text = test_tweet)