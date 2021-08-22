from flask import Blueprint, render_template, jsonify, request
import pickle

graduation = Blueprint('graduation',__name__)

# bachelor
model_graduation_bachelor_fifth   = pickle.load(open("model/graduation/bachelor/Semester5.pkl", "rb"))
model_graduation_bachelor_sixth   = pickle.load(open("model/graduation/bachelor/Semester6.pkl", "rb"))
model_graduation_bachelor_seventh = pickle.load(open("model/graduation/bachelor/Semester7.pkl", "rb"))

# diploma
model_graduation_diploma_third  = pickle.load(open("model/graduation/diploma/Semester3.pkl", "rb"))
model_graduation_diploma_fourth = pickle.load(open("model/graduation/diploma/Semester4.pkl", "rb"))
model_graduation_diploma_fifth  = pickle.load(open("model/graduation/diploma/Semester5.pkl", "rb"))

# graduation page
@graduation.route("/graduation")
def graduation_index():
    data = {
        "title": "Prediksi Kelulusan"
    }
    return render_template("graduation/index.html", data=data)

# bachelor
@graduation.route("/graduation/bachelor")
def graduation_bachelor_index():
    data = {
        "title": "Prediksi Kelulusan Bachelor"
    }
    return render_template("graduation/bachelor/index.html", data=data)

@graduation.route("/graduation/bachelor/fifth")
def graduation_bachelor_five_semesters():
    data = {
        "title": "Prediksi 5 Semester"
    }
    return render_template("graduation/bachelor/five-semesters.html", data=data)

@graduation.route("/graduation/bachelor/sixth")
def graduation_bachelor_six_semesters():
    data = {
        "title": "Prediksi 6 Semester"
    }
    return render_template("graduation/bachelor/six-semesters.html", data=data)

@graduation.route("/graduation/bachelor/seventh")
def graduation_bachelor_seven_semesters():
    data = {
        "title": "Prediksi 7 Semester"
    }
    return render_template("graduation/bachelor/seven-semesters.html", data=data)


# diploma
@graduation.route("/graduation/diploma")
def graduation_diploma_index():
    data = {
        "title": "Prediksi Kelulusan Diploma"
    }
    return render_template("graduation/diploma/index.html", data=data)

@graduation.route("/graduation/diploma/third")
def graduation_diploma_three_semesters():
    data = {
        "title": "Prediksi 3 Semester Diploma"
    }
    return render_template("graduation/diploma/three-semesters.html", data=data)

@graduation.route("/graduation/diploma/fourth")
def graduation_diploma_four_semesters():
    data = {
        "title": "Prediksi 4 Semester Diploma"
    }
    return render_template("graduation/diploma/four-semesters.html", data=data)

@graduation.route("/graduation/diploma/fifth")
def graduation_diploma_five_semesters():
    data = {
        "title": "Prediksi 5 Semester"
    }
    return render_template("graduation/diploma/five-semesters.html", data=data)


# predict
@graduation.route("/graduation/bachelor/predict", methods=['POST'])
def graduation_bachelor_predict():
    prediction = [-2]
    if request.form['jumlah_semester'] == 'five':
        data_form = [
            request.form['semester_1'],
            request.form['semester_2'],
            request.form['semester_3'],
            request.form['semester_4'],
            request.form['semester_5'],
        ]
        value = [data_form]
        prediction = model_graduation_bachelor_fifth.predict(value)
    elif (request.form['jumlah_semester'] == 'six'):
        data_form = [
            request.form['semester_1'],
            request.form['semester_2'],
            request.form['semester_3'],
            request.form['semester_4'],
            request.form['semester_5'],
            request.form['semester_6'],
        ]
        value = [data_form]
        prediction = model_graduation_bachelor_sixth.predict(value)
    elif (request.form['jumlah_semester'] == 'seven'):
        data_form = [
            request.form['semester_1'],
            request.form['semester_2'],
            request.form['semester_3'],
            request.form['semester_4'],
            request.form['semester_5'],
            request.form['semester_6'],
            request.form['semester_7'],
        ]
        value = [data_form]
        prediction = model_graduation_bachelor_seventh.predict(value)
    predictionMap = {}
    predictionMap[2] = "Sangat Memuaskan"
    predictionMap[1] = "Memuaskan"
    predictionMap[0] = "Cumlaude"
    predictionMap[-1] = "Tidak Lulus"
    predictionMap[-2] = "Error"

    data = {
        "title": "Prediksi Sarjana",
        "prediction": predictionMap[prediction[0]]
    }

    return render_template("graduation/bachelor/predict.html", data=data)

@graduation.route("/api/v1/graduation/bachelor/predict", methods=['POST'])
def graduation_bachelor_predict_api():
    try:
        if request.get_json() is None or request.get_json()['nilai'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Need correct request"
            }

            return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Need correct request"
            }

        return jsonify(data)

    length_semester = len(request.get_json()['nilai'])
    value = [request.get_json()['nilai']]

    if length_semester < 5 or length_semester > 7:
        data = {
            "status": False,
            "response_code": 400,
            "message": "Doesn't meet the criteria length semester min 5 and max 7"
        }

        return jsonify(data)

    if length_semester == 5:
        prediction = model_graduation_bachelor_fifth.predict(value)
    elif length_semester == 6:
        prediction = model_graduation_bachelor_sixth.predict(value)
    elif length_semester == 7:
        prediction = model_graduation_bachelor_seventh.predict(value)
    
    predictionMap = {}
    predictionMap[2] = "Sangat Memuaskan"
    predictionMap[1] = "Memuaskan"
    predictionMap[0] = "Cumlaude"
    predictionMap[-1] = "Tidak Lulus"
    predictionMap[-2] = "Error"

    data = {
        "prediction": predictionMap[prediction[0]],
        "status": True,
        "response_code": 200,
        "message": "The request has succeeded. An entity corresponding to the requested resource is sent in the response."
    }

    return jsonify(data)

@graduation.route("/graduation/diploma/predict", methods=['POST'])
def graduation_diploma_predict():
    prediction = [-2]
    if request.form['jumlah_semester'] == '3':
        data_form = [
            request.form['semester_1'],
            request.form['semester_2'],
            request.form['semester_3'],
        ]
        value = [data_form]
        prediction = model_graduation_diploma_third.predict(value)
    elif (request.form['jumlah_semester'] == '4'):
        data_form = [
            request.form['semester_1'],
            request.form['semester_2'],
            request.form['semester_3'],
            request.form['semester_4'],
        ]
        value = [data_form]
        prediction = model_graduation_diploma_fourth.predict(value)
    elif (request.form['jumlah_semester'] == '5'):
        data_form = [
            request.form['semester_1'],
            request.form['semester_2'],
            request.form['semester_3'],
            request.form['semester_4'],
            request.form['semester_5'],
        ]
        value = [data_form]
        prediction = model_graduation_diploma_fifth.predict(value)
    predictionMap = {}
    predictionMap[2] = "Sangat Memuaskan"
    predictionMap[1] = "Memuaskan"
    predictionMap[0] = "Cumlaude"
    predictionMap[-1] = "Tidak Lulus"
    predictionMap[-2] = "Error"

    data = {
        "title": "Prediksi Sarjana",
        "prediction": predictionMap[prediction[0]]
    }

    return render_template("graduation/bachelor/predict.html", data=data)

@graduation.route("/api/v1/graduation/diploma/predict", methods=['POST'])
def graduation_diploma_predict_api():
    try:
        if request.get_json() is None or request.get_json()['nilai'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Need correct request"
            }

            return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Need correct request"
            }

        return jsonify(data)

    length_semester = len(request.get_json()['nilai'])
    value = [request.get_json()['nilai']]

    if length_semester < 3 or length_semester > 5:
        data = {
            "status": False,
            "response_code": 400,
            "message": "Doesn't meet the criteria length semester min 3 and max 5"
        }

        return jsonify(data)

    if length_semester == 3:
        prediction = model_graduation_diploma_third.predict(value)
    elif length_semester == 4:
        prediction = model_graduation_diploma_fourth.predict(value)
    elif length_semester == 5:
        prediction = model_graduation_diploma_fifth.predict(value)
    
    predictionMap = {}
    predictionMap[2] = "Sangat Memuaskan"
    predictionMap[1] = "Memuaskan"
    predictionMap[0] = "Cumlaude"
    predictionMap[-1] = "Tidak Lulus"
    predictionMap[-2] = "Error"

    data = {
        "prediction": predictionMap[prediction[0]],
        "status": True,
        "response_code": 200,
        "message": "The request has succeeded. An entity corresponding to the requested resource is sent in the response."
    }

    return jsonify(data)