import os
import json
from datetime import datetime

import tweepy
import configparser

DATASET_DIR = 'datasets'
EXPERIMENT_DIR = 'combfreq'
RESULTS = os.path.join(DATASET_DIR, EXPERIMENT_DIR, 'simulation_results_scaled_tf.json')

today = datetime.now()
start = datetime(2021, 6, 19)
delta = today - start
day = str(delta.days)

config = configparser.ConfigParser()
config.read('.env')

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = config['oauth']['CONSUMER_KEY']
CONSUMER_SECRET = config['oauth']['CONSUMER_SECRET']
ACCESS_KEY = config['oauth']['ACCESS_KEY']
ACCESS_SECRET = config['oauth']['ACCESS_SECRET']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

with open(RESULTS, "r", encoding='utf8') as file:
    results = json.load(file)

current_answer = results["games"][day]["share"]
api.update_status(current_answer)
