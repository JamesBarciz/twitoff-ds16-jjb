"""Main app/routing file for TwitOff."""

# Package imports
from flask import Flask, render_template

# Local imports
from .models import DB, User, Tweet, add_test_users, add_test_tweets
from .twitter import add_users


def create_app():
    """Creates and configures an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')
    
    @app.route('/add_test_users')
    def add_users():
        DB.drop_all()
        DB.create_all()
        add_test_users()
        return 'Users added!'
    
    @app.route('/add_test_tweets')
    def add_tweets():
        DB.drop_all()
        DB.create_all()
        add_test_tweets()
        return 'Tweets added!'

    @app.route('/view_test_users')
    def view_users():
        users = User.query.all()
        return '<br/>'.join([str(user) for user in users])
    
    @app.route('/view_test_tweets')
    def view_tweets():
        tweets = Tweet.query.all()
        return '<br/>'.join([str(tweet) for tweet in tweets])

    return app
