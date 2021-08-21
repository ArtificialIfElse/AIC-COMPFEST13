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
tokenizer = pickle.load(open("model/tokenizer_abstract.pkl", "rb"))
model = load_model('model/paper_abstract.h5')

# Padding

topic = ['AI/ML',	'Computer Science',
         'Computer Vision',	'Math & Stats',	'Physics']


def get_category(abstract):
    abstract = tokenizer.texts_to_sequences(abstract)
    abstract = pad_sequences(abstract, maxlen=10000)
    prediction = model.predict(abstract)
    print(np.argmax(prediction))
    print(topic[np.argmax(prediction)])


tex2 = "As computer vision has become a part of our daily life. Using smartphones features like face recognition is all a part of computer vision. In this paper, we will talk aboutCV or Computer Vision which is preferably used to read and display a video stream in real time through which one can access the web camera and using machine learning one can let their system learn through data sent by user or through datasets which is easily available on the internet and then system trains itself. After training part it is ready to solve the real life problems. But using both computer vision and machine learning at the same time is always a challenging task asone has to capture and another has to train the system at the same timeso that the system could be able to recognize the things to which they are trained is the most innovative work in this paper as we have to keep in mind that both the things should be done at the same time"
get_category([tex2])
