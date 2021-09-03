# Import modules
import numpy as np
import tweepy
import pickle
import warnings
warnings.filterwarnings('ignore')

# Mengkoneksikan twitter API dengan tweepy
CONSUMER_KEY = 'zzzzzzzzzzzzzzz'
CONSUMER_SECRET = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
ACCESS_TOKEN = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
ACCESS_TOKEN_SECRET = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(AUTH)

# Import model
ieModel = pickle.load(open("model/ieModel.pkl", "rb"))
nsModel = pickle.load(open("model/nsModel.pkl", "rb"))
ftModel = pickle.load(open("model/ftModel.pkl", "rb"))
pjModel = pickle.load(open("model/pjModel.pkl", "rb"))
cv = pickle.load(open('model/cv_vectorizer.pkl', 'rb'))


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


# Contoh
print(search_trait('TomCruise'))
print(search_trait('handhikayp'))
