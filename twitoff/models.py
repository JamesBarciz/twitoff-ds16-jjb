#!/usr/bin/env Python
"""SQLAlchemy models and utility functions for TwitOff."""

# Package imports
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                 'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                 'common_squirrel', 'KenJennings', 'conanobrien',
                 'big_ben_clock', 'IAM_SHAKESPEARE']

TWITTER_TWEETS = ['Lol, whatever!', 'Hello!', 'No way!', 'GTFO', 'Hi!',
                  'Hey', 'dsajk', 'awlk', 'dajwdia', 'awihajiw', 'wah',
                  'weikajdo', 'wiadawjao', 'fourteen']


class User(DB.Model):
    """Twitter users."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    # Tweet IDs are ordinal ints, so can be used to fetch only more recent
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f'[User {self.name}]'


class Tweet(DB.Model):
    """User tweets and their embeddings from Basilica."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))

    def __repr__(self):
        return f'[Tweet: {self.text}]'


def add_test_users():
    for i, name in enumerate(TWITTER_USERS):
        user = User(id=i, name=name)
        DB.session.add(user)
    DB.session.commit()

def add_test_tweets():
    for i, text in enumerate(TWITTER_TWEETS):
        tweet = Tweet(id=i, full_text=text)
        DB.session.add(tweet)
    DB.session.commit()
