from flask import Flask, request, jsonify, render_template
# import pandas as pd
from graduation import *
import numpy as np
import os

flask_app = Flask(__name__)
flask_app.register_blueprint(graduation)

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

@flask_app.route("/paper/predict")
def paper_predict():
    data = {
        "title": "Prediksi Tema Paper"
    }
    return render_template("paper/predict.html", data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port, debug=True)



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