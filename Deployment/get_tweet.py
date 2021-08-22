# Import modules
import numpy as np
import tweepy
import pickle
import warnings
warnings.filterwarnings('ignore')

# Mengkoneksikan twitter API dengan tweepy
CONSUMER_KEY = 'ATynlkRJqVZDxlUaSP3PLHnR8'
CONSUMER_SECRET = 'V6m3201858NwLl6ZUGEIyGaDgZpKquyrYeY2TsmC7m2zlJ3lYJ'
ACCESS_TOKEN = '2418452160-vGpbJIRosoKLplkABXFKWAFVRuQFljiVumfDa3x'
ACCESS_TOKEN_SECRET = 'XlWzD3E6XfQiXF3QjxqbQDaSoYByp6cu7IcBzZjaUIHLd'

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(AUTH)

# Import model
ieModel = pickle.load(open("model/twitter/ieModel.pkl", "rb"))
nsModel = pickle.load(open("model/twitter/nsModel.pkl", "rb"))
ftModel = pickle.load(open("model/twitter/ftModel.pkl", "rb"))
pjModel = pickle.load(open("model/twitter/pjModel.pkl", "rb"))
cv = pickle.load(open('model/twitter/cv_vectorizer.pkl', 'rb'))


# Fungsi untuk memperoleh username
def search_trait(username):
    trait = []
    tweets = api.user_timeline(f'{username}', count=150)
    tweets = [tweet.text for tweet in tweets]

    document = cv.transform([' '.join(tweets)])

    trait.append(ieModel.predict(document))
    trait.append(nsModel.predict(document))
    trait.append(ftModel.predict(document))
    trait.append(pjModel.predict(document))

    return "".join(np.concatenate(trait))