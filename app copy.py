from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/api/classify-number")
def classify_number(n):   
    data = {
            "number": n,
            "is_prime": "false",
            }
    return jsonify(data)
