import tweepy
import configparser


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

api.update_status("Wordle 264 4/6*\n\n⬛🟩⬛🟨🟨\n⬛🟩⬛🟩🟩\n⬛🟩🟨🟩🟩\n🟩🟩🟩🟩🟩\n" )