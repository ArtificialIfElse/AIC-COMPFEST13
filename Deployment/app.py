from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

flask_app = Flask(__name__)
# model_personality = pickle.load(open("personality.pkl", "rb"))
model_kelulusan = pickle.load(open("graduation_s1_six.pkl", "rb"))

@flask_app.route("/")
def index():
    data = {
        "title": "Pra Kuliah"
    }
    return render_template("home.html", data=data)

# personality page
@flask_app.route("/personality")
def personality_index():
    data = {
        "title": "Prediksi Personality"
    }
    return render_template("personality/index.html", data=data)

@flask_app.route("/personality/test")
def personality_check():
    data = {
        "title": "Test Personality"
    }
    return render_template("personality/test.html", data=data)

# graduation page
@flask_app.route("/graduation")
def graduation_index():
    data = {
        "title": "Prediksi Kelulusan"
    }
    return render_template("graduation/index.html", data=data)

@flask_app.route("/graduation/bachelor")
def graduation_index():
    data = {
        "title": "Prediksi Kelulusan"
    }
    return render_template("graduation/index.html", data=data)

@flask_app.route("/graduation/bachelor/fifth")
def graduation_bachelor_five_semesters():
    data = {
        "title": "Prediksi 5 Semester"
    }
    return render_template("graduation/five-semesters.html", data=data)

@flask_app.route("/graduation/bachelor/sixth")
def graduation_bachelor_six_semesters():
    data = {
        "title": "Prediksi 6 Semester"
    }
    return render_template("graduation/six-semesters.html", data=data)

@flask_app.route("/graduation/bachelor/seventh")
def graduation_bachelor_seven_semesters():
    data = {
        "title": "Prediksi 7 Semester"
    }
    return render_template("graduation/seven-semesters.html", data=data)



# semester six
@flask_app.route("/graduation/bachelor/predict")
def graduation_bachelor_predict():
    value = [[3.0, 3.5, 4.0, 3.0, 2.5, 2.0]]
    # df = pd.DataFrame(value)
    prediction = model_kelulusan.predict(value)
    # print(prediction[0])

    predictionMap = {}
    predictionMap[2] = "Sangat Memuaskan"
    predictionMap[1] = "Memuaskan"
    predictionMap[0] = "Cumlaude"
    predictionMap[-1] = "Tidak Lulus"

    data = {
        "title": "Prediksi 5 Semester",
        "prediction": predictionMap[prediction[0]]
    }

    return render_template("graduation/predict.html", data=data)

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

@flask_app.route("/paper/predict")
def paper_predict():
    data = {
        "title": "Prediksi Tema Paper"
    }
    return render_template("paper/predict.html", data=data)

if __name__ == "__main__":
    flask_app.run(debug=True)



# @flask_app.route("/")
# def Home():
    # index = ["IPS1", "IPS2", "IPS3", "IPS4", "IPS5", "IPS6", "IPS7", "IPS8", "LS"]

    # value = [3, 3, 3, 3, 3, 3, 3, 3, 8]

    # df = pd.DataFrame(value, index=value)

    # predict = model.predict(df.T)
#     return render_template("index.html")

    # value = [3.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 3.0,
    #         1.0, 1.0, 1.0, 3.0, 1.0, 3.0, 1.0, 1.0, 2.0, 1.0, 1.0, 3.0, 1.0,
    #         1.0, 3.0, 3.0, 3.0, 2.0, 3.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0,
    #         1.0, 3.0, 1.0, 3.0, 1.0, 3.0, 1.0, 3.0, 3.0, 1.0, 3.0]
    
    # value = [
    #     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #     4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
    #     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    # ]
        # print(request.form.values())
    # float_features = [float(x) for x in request.form.values()]
    # features = [np.array(float_features)]
    # index = ["EXT1", "EXT2", "EXT3", "EXT4", "EXT5", "EXT6", "EXT7", "EXT8", "EXT9", "EXT10",
    #          "EST1", "EST2", "EST3", "EST4", "EST5", "EST6", "EST7", "EST8", "EST9", "EST10",
    #          "AGR1", "AGR2", "AGR3", "AGR4", "AGR5", "AGR6", "AGR7", "AGR8", "AGR9", "AGR10",
    #          "CSN1", "CSN2", "CSN3", "CSN4", "CSN5", "CSN6", "CSN7", "CSN8", "CSN9", "CSN10",
    #          "OPN1", "OPN2", "OPN3", "OPN4", "OPN5", "OPN6", "OPN7", "OPN8", "OPN9", "OPN10"
    #         ]
    # features = [[1, 2, 3, 4, 5, 2, 3, 4, 2, 2, 
    #             3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 
    #             1, 2, 3, 4, 3, 2, 4, 2, 1, 1,
    #             1, 2, 3, 4, 3, 2, 4, 2, 1, 1,
    #             1, 2, 3, 4, 3, 2, 4, 2, 1, 1]]