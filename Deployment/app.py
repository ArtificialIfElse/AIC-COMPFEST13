from flask import Flask, request, jsonify, render_template
# import pandas as pd
from graduation import *
from personality import *
from twitter import *
from paper import *
import numpy as np
import os

flask_app = Flask(__name__)
flask_app.register_blueprint(graduation)
flask_app.register_blueprint(personality)
flask_app.register_blueprint(twitter)
flask_app.register_blueprint(paper)

@flask_app.route("/")
def index():
    data = {
        "title": "Homepage",
        "selected": "index"
    }
    return render_template("home.html", data=data)

@flask_app.route('/api-docs')
def api_docs():
    data = {
        "title": "API Documentation",
        "selected": "api_docs"
    }
    return render_template("api_docs.html", data=data)

@flask_app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@flask_app.route('/about')
def about():
    data = {
        "title": "About ArtificialIfElse"
    }

    return render_template("about.html", data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port, debug=True)
