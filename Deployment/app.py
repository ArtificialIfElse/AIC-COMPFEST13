from flask import Flask, request, jsonify, render_template
# import pandas as pd
from graduation import *
from personality import *
from twitter import *
from paper import *
import numpy as np
import os

flask_app = Flask(__name__)
flask_app.register_blueprint(graduation)
flask_app.register_blueprint(personality)
flask_app.register_blueprint(twitter)
flask_app.register_blueprint(paper)

@flask_app.route("/")
def index():
    data = {
        "title": "Pra Prediksi Kelulusan"
    }
    return render_template("home.html", data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port, debug=True)
