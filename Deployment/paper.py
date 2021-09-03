from flask import Flask, json, request, jsonify, render_template
from personality_logic import *

from flask import Blueprint, render_template, jsonify, request
from paper_topic_predictions import *
from googletrans import Translator
import numpy as np

# learn
from transformers import pipeline

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
    classifier = pipeline("zero-shot-classification")
    result = classifier(abstract, 
           candidate_labels=['AI/ML', 'Cyber Security', 'DevOps', 'Cryptography', 'Mathematics', 'Statistics', 'Physics', 'Social'])

    label = result["labels"][0]
    best_score = np.round(result["scores"][0] * 100)

    data = {
        "title": "Prediksi Tema Paper",
        "selected": "paper",
        "scores": result["scores"],
        "labels": result["labels"],
        "best_score": best_score,
        "best_label": label
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
        classifier = pipeline("zero-shot-classification")
        result = classifier(abstract, 
           candidate_labels=['AI/ML', 'Cyber Security', 'DevOps', 'Cryptography', 'Mathematics', 'Statistics', 'Physics', 'Social'])

        best_label = result["labels"][0]
        best_score = np.round(result["scores"][0] * 100)

        data_result = []
        for iterate in range(len(result["labels"])):
            data_result.append({
                'label': result["labels"][iterate],
                'score': result["scores"][iterate]
            })

        data = {
                "status": True,
                "response_code": 200,
                "message": "Success Predict Paper Theme",
                "best_score": best_score,
                "best_label": best_label,
                "data": data_result
            }

        return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }
        return jsonify(data)
