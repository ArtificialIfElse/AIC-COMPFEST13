from flask import Flask, request, jsonify, render_template
# import pandas as pd
from graduation import *
from personality import *
import numpy as np
import os

flask_app = Flask(__name__)
flask_app.register_blueprint(graduation)
flask_app.register_blueprint(personality)

@flask_app.route("/")
def index():
    data = {
        "title": "Pra Prediksi Kelulusan"
    }
    return render_template("home.html", data=data)

# paper page
@flask_app.route("/paper")
def paper_index():
    data = {
        "title": "Prediksi Tema Paper"
    }
    return render_template("paper/index.html", data=data)

@flask_app.route("/paper/check")
def paper_check():
    data = {
        "title": "Prediksi Tema Paper"
    }
    return render_template("paper/check.html", data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port, debug=True)
