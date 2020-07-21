#!/usr/bin/env Python
"""Retrieve Tweets, embeddings, and persist in the database."""
import tweepy
import basilica
import os
from dotenv import load_dotenv

from .models import DB, Tweet, User, TWITTER_USERS

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET")
BASILICA_KEY = os.getenv("BASILICA_KEY")

TWITTER_AUTH = tweepy.OAuthHandler(
    API_KEY,
    API_SECRET_KEY
)
TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(BASILICA_KEY)


def add_or_update_user(username):
    """Add or update a user and their Tweets, error if not a Twitter user."""
    try:
        twitter_user = TWITTER.get_user(username)
        db_user = (User.query.get(twitter_user.id) or
                   User(id=twitter_user.id, name=username))
        DB.session.add(db_user)
        # We want as many recent non-retweet/reply statuses as we can get
        # 200 is a Twitter API limit, we'll usually see less due to exclusions
        tweets = twitter_user.timeline(
            count=200, exclude_replies=True, include_rts=False,
            tweet_mode='extended', since_id=db_user.newest_tweet_id)
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet.full_text,
                                                model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300],
                             embedding=embedding)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print(f'Error processing {username}: {e}')
        raise e
    else:
        DB.session.commit()


def add_users(users=TWITTER_USERS):
    """Add/update a list of users."""
    # for user in users:
    #     add_or_update_user(user)
    add_or_update_user(users[0])


def update_all_users():
    """Update all existing users."""
    for user in User.query.all():
        add_or_update_user(user.name)
