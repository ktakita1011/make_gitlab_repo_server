import os
import sys

from flask import Flask
from flask_cors import CORS

def create_app():
    app_ = Flask(__name__)
    CORS(app_)
    app_.config["JSON_AS_ASCII"] = False
    return app_

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)