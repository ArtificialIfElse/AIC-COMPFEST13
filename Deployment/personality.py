from flask import Flask, json, request, jsonify, render_template
from personality_logic import *

from flask import Blueprint, render_template, jsonify, request

personality = Blueprint('personality',__name__)

@personality.route("/personality")
def index_personality():
    data = {
        "title": "Cari tahu tentang kamu",
        "selected": "personality"
    }

    return render_template("personality/index.html", data=data)

@personality.route("/personality/question")
def questions_personality():
    questions = get_list_pertanyaan()
    data = {
        "title": "Pertanyaan untukmu",
        "questions": questions,
        "selected": "personality",
        "length_questions": len(questions)
    }

    return render_template("personality/questions.html", data=data)

@personality.route("/api/v1/personality/get_questions", methods=['GET'])
def get_question():
    questions = get_list_pertanyaan()
    list_questions = []
    iterate = 1
    for item in questions:
        each_question = {}
        each_question["nama_soal"] = "soal" + str(iterate)
        each_question["soal"] = item
        each_question["value_slider"] = 0
        list_questions.append(each_question)
        iterate += 1

    data = {
        "data": list_questions,
        "status": True,
        "response_code": 200,
        "message": "The request has succeeded. An entity corresponding to the requested resource is sent in the response."
    }

    return jsonify(data)

@personality.route("/personality/predict", methods=["POST"])
def predict_personality():
    lastfix = []
    for x in range(1, 51):
        lastfix.append(str(x))
    answer = []
    for data in lastfix:
        answer.append(request.form['question' + str(data)])

    result = extract_personality_model(answer)
    data = {
        "title": "Prediksi Personality",
        "selected": "personality",
        "result": result
    }
    return render_template("personality/predict.html", data=data)

@personality.route("/api/v1/personality/predict", methods=['POST'])
def get_personality_mbti():
    try:
        if request.get_json() is None or request.get_json()['answer'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Need correct request"
            }

            return jsonify(data)
        if len(request.get_json()['answer']) > 50 or len(request.get_json()['answer']) < 50:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }

            return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Need correct request"
            }
        return jsonify(data)
    result = extract_personality_model(request.get_json()['answer'])

    data = {
        "mbti": result['mbti'],
        "advice": result['advice'],
        "recommendation_major": result['recommendation_major'],
        "agreeableness": result['graph_plot']['agreeableness'],
        "extroversion": result['graph_plot']['extroversion'],
        "conscientiousness": result['graph_plot']['conscientiousness'],
        "neuroticism": result['graph_plot']['neuroticism'],
        "openness": result['graph_plot']['openness'],
        "status": True,
        "response_code": 200,
        "message": "The request has succeeded. An entity corresponding to the requested resource is sent in the response."
    }

    return jsonify(data)

def get_list_pertanyaan():
    questions = [
        "Saya tipe orang penyuka pesta",
        "Saya tidak banyak bicara",
        "Saya merasa nyaman berada di dekat banyak orang",
        "Saya memilih menyembunyikan latar belakang diri saya",
        "Saya tipe orang yang memulai percakapan",
        "Saya tidak punya banyak hal untuk dikatakan",
        "Saya berbicara dengan banyak orang yang berbeda di pesta",
        "Saya tidak suka menarik perhatian orang lain terhadap diri saya",
        "Saya tidak keberatan menjadi pusat perhatian",
        "Saya pendiam di sekitar orang asing",
        "Saya mudah stres",
        "Saya sering bersantai",
        "Saya mengkhawatirkan banyak hal",
        "Saya jarang merasa sedih",
        "Saya mudah terganggu",
        "Saya mudah marah",
        "Saya sering mengubah suasana hati diri saya",
        "Saya sering mengalami perubahan suasana hati",
        "Saya mudah tersinggung",
        "Saya sering merasa sedih",
        "Saya merasa sedikit tidak peduli terhadap orang lain",
        "Saya tertarik pada orang lain",
        "Saya suka menghina orang",
        "Saya bersimpati dengan perasaan orang lain",
        "Saya tidak tertarik dengan masalah orang lain",
        "Saya memiliki hati yang lembut",
        "Saya tidak terlalu tertarik dengan orang lain",
        "Saya meluangkan waktu untuk orang lain",
        "Saya dapat merasakan emosi orang lain",
        "Saya mampu membuat orang merasa nyaman",
        "Saya selalu siap",
        "Saya meninggalkan barang disekitar secara acak",
        "Saya memperhatikan detail",
        "Saya tipe orang pembuat kekacauan",
        "Saya segera menyelesaikan tugas",
        "Saya sering lupa mengembalikan barang ke tempatnya",
        "Saya menyukai ketertiban",
        "Saya melalaikan tugas saya",
        "Saya tipe orang yang mengikuti jadwal",
        "Saya bersikap penuntut dalam pekerjaan",
        "Saya memiliki banyak kosakata",
        "Saya kesulitan memahami ide-ide bersifat abstrak",
        "Saya memiliki imajinasi yang jelas",
        "Saya tidak tertarik dengan ide-ide bersifat abstrak",
        "Saya punya ide bagus",
        "Saya tidak memiliki imajinasi yang baik",
        "Saya cepat memahami banyak hal",
        "Saya menggunakan kata-kata sulit",
        "Saya menghabiskan waktu untuk merenungkan berbagai hal",
        "Saya penuh dengan ide"
    ]

    return questions