from flask import Flask, jsonify, request
from helpers import is_prime, is_perfect, properties, digit_sum, fun_fact
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.json.sort_keys = False
cors = CORS(app) 


@app.route('/api/classify-number', methods=['GET'])
@cross_origin()
def classify_number():  
    n = request.args.get('number')
    try:
        n = int(n)
        data = {
                "number": n,
                "is_prime": is_prime(n),
                "is_perfect": is_perfect(n),
                "properties": properties(n),
                "digit_sum": digit_sum(abs(n)),
                "fun_fact": fun_fact(n)
                }
        return jsonify(data), 200
    except (ValueError, TypeError):
        return jsonify({"number": n, "error": True}), 400

@app.route("/")
def index():
    return "Welcome"