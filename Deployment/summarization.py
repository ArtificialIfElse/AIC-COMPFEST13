from flask import Blueprint, render_template, jsonify, request
from transformers import pipeline
from googletrans import Translator

summarization = Blueprint('summarization',__name__)

@summarization.route("/summarization")
def summarization_index():
    data = {
        "title": "Summarization Papermu",
        "selected": "paper"
    }

    return render_template("summarization/index.html", data=data)

@summarization.route("/summarization/check")
def summarization_check():
    data = {
        "title": "Check Summarization Papermu",
        "selected": "paper"
    }

    return render_template("summarization/check.html", data=data)

@summarization.route("/summarization/predict", methods=["POST"])
def summarization_predict():
    summary = ""

    summary = request.form['abstract']

    summarizer = pipeline("summarization")
    result_summary = summarizer(summary)

    print(summarizer)

    data = {
        "title": "Hasil Summarization Papermu",
        "selected": "paper",
        "summary_text": result_summary[0]["summary_text"]
    }

    return render_template("summarization/predict.html", data=data)
