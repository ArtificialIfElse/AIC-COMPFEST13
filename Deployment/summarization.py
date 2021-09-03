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

    data = {
        "title": "Hasil Summarization Papermu",
        "selected": "paper",
        "summary_text": result_summary[0]["summary_text"]
    }

    return render_template("summarization/predict.html", data=data)

@summarization.route("/api/v1/summarization/predict", methods=["POST"])
def api_predict_summarization():
    try:
        if request.get_json() is None or request.get_json()['abstract'] is None or request.get_json()['language'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }

            return jsonify(data)
        summary = request.get_json()['abstract']
        summarizer = pipeline("summarization")
        result_summary = summarizer(summary)
        data = {
                "status": True,
                "response_code": 200,
                "message": "Success Summarization Paragraph",
                "summary_text": result_summary[0]["summary_text"]
            }

        return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }
        return jsonify(data)
