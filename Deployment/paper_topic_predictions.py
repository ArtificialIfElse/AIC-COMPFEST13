# Data Preprocessing
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load model
from keras.models import load_model
import pickle

# Remove warnings
import warnings
warnings.filterwarnings('ignore')

# Tokenisasi
tokenizer = pickle.load(open("model/paper/tokenizer_abstract.pkl", "rb"))
model = load_model('model/paper/paper_abstract.h5')

# Padding
topic = ['AI/ML',	'Computer Science',
         'Computer Vision',	'Math & Stats',	'Physics']


def get_category(abstract):
    abstract = tokenizer.texts_to_sequences(abstract)
    abstract = pad_sequences(abstract, maxlen=10000)
    prediction = model.predict(abstract)
    
    return topic[np.argmax(prediction)]

