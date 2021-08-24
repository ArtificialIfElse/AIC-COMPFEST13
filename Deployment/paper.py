from flask import Flask, json, request, jsonify, render_template
from personality_logic import *

from flask import Blueprint, render_template, jsonify, request
from paper_topic_predictions import *
from googletrans import Translator

paper = Blueprint('paper',__name__)

# paper page
@paper.route("/paper")
def paper_index():
    data = {
        "title": "Prediksi Tema Paper",
        "selected": "paper"
    }
    return render_template("paper/index.html", data=data)

@paper.route("/paper/request-predict")
def request_predict():
    data = {
        "title": "Masukkan Hasil Paper Kamu",
        "selected": "paper"
    }

    return render_template("paper/request-paper.html", data=data)

@paper.route("/paper/predict", methods=["POST"])
def predict_paper():
    abstract = request.form['abstract']
    language = request.form['language']

    if language == 2:
        translator = Translator()
        result_translate = translator.translate(abstract, dest='en')
        abstract = result_translate.text
    result = get_category([abstract])

    data = {
        "title": "Prediksi Tema Paper",
        "selected": "paper",
        "prediction": result
    }

    return render_template("paper/predict.html", data=data)

@paper.route("/api/v1/paper/predict", methods=["POST"])
def api_predict_paper():
    try:
        if request.get_json() is None or request.get_json()['abstract'] is None or request.get_json()['language'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }

            return jsonify(data)

        abstract = request.get_json()['abstract']
        if (request.get_json()['language'] == 2):
            translator = Translator()
            result_translate = translator.translate(abstract, dest='en')
            abstract = result_translate.text

        result = get_category([abstract])

        data = {
                "status": True,
                "response_code": 200,
                "message": "Success Predict Paper Theme",
                "theme": result
            }

        return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }
        return jsonify(data)
