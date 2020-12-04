# Twit-Off
A Flask web application which aims to predict, between two Twitter users, who is more likely to post a given Tweet.

## Tech Stack
---
This application is primarily written in *Python* however, the webpages are written with *HTML incorporating Python*.  

*Tweepy* is used in this application (in tandem with developer API access) to connect to the Twitter API to obtain user Tweets.

The microframework used to build this application is *Flask* and eventually, with the help of *Gunicorn*, will be deployed to Heroku.

The database is a *PostgreSQL* server generated through Heroku's *hobbydev* option and hosted with *AWS*.

This application also uses *Flask SQLAlchemy* which is an ORM (object-relational-mapper) that assists in the creation of the database and insertion of data via the front-end.

User Tweets are stored as embeddings in the Postgres database and are processed using NLP (Natural Language Processing) with *SpaCy*'s word vectorizer and *en_core_web_lg* model.  Formerly, Tweets were embedded using *Basilica* and code can be changed to facilitate this should Basilica.ai become accessible again.

Finally, the model used to predict Twitter users is a simple *Logistic Regression* model from *Scikit Learn*.

## Directory Structure
---
```
├─ twitoff                    → App Directory
│   ├─ templates              → HTML Templates
│   │    ├─ base.html         → Base Webpage
│   │    ├─ prediction.html   → Prediction Page
│   │    └─ user.html         → User Tweets Page
│   │
│   ├─ app.py                 → Main Application
│   ├─ hello.py
│   ├─ models.py              → SQLAlchemy Model
│   ├─ predict.py             → Logistic Regression Model
│   └─ twitter.py             → Twitter API Authentication
│
├─ .gitignore
├─ LICENSE
├─ Pipfile
├─ Pipfile.lock
├─ Procfile
├─ README.md
├─ TwitOff Application Architecture.pdf
├─ TwitOff Database Entity Relationship Diagram.pdf
└─ requirements.txt
```