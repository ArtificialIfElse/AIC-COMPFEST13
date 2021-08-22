from flask import Blueprint, json, render_template, jsonify, request
import pickle
from get_tweet import *

twitter = Blueprint('twitter',__name__)

# graduation page
@twitter.route("/twitter")
def twitter_index():
    data = {
        "title": "Prediksi lewat username twitter"
    }
    return render_template("twitter/index.html", data=data)

@twitter.route("/twitter/predict", methods=["POST"])
def twitter_predict():
    username = request.form["username"]
    try:
        result = search_trait(username)
    except:
        data = {
            "title": "Prediksi lewat username twitter",
            "prediction": "Username tidak ditemukan",
            "is_found": False
        }
        return render_template("twitter/predict.html", data=data)
    data = {
        "title": "Prediksi lewat username twitter",
        "prediction": result,
        "is_found": True
    }
    return render_template("twitter/predict.html", data=data)

@twitter.route("/api/v1/twitter/predict", methods=["POST"])
def api_twitter_predict():
    try:
        if request.get_json() is None or request.get_json()['username'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }

            return jsonify(data)

        username = request.get_json()['username']
        try:
            result = search_trait(username)
        except:
            data = {
                "status": False,
                "response_code": 404,
                "message": "Username Not Found",
                "is_found": False,
                "personality": ""
            }

            return jsonify(data)

        data = {
                "status": True,
                "response_code": 200,
                "message": "Success Predict Personality by username twitter",
                "is_found": True,
                "personality": result
            }

        return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }
        return jsonify(data)