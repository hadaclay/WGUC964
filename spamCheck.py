from joblib import load
from flask import jsonify
import numpy as np

spam_model = load('static/model.joblib')


def checkSpam(data):
    return jsonify(int(spam_model.predict([data.get('message')])[0]))
