# from flask import Flask, jsonify
# import requests
# query_params = {"#":42, "type":"trivia"}

# response = requests.get("http://numbersapi.com/42/math")
# print(response.text)

curl -v --request OPTIONS 'http://127.0.0.1:5000/api/classify-number?number=371' -H 'Origin: https://google.com' -H 'Access-Control-Request-Method: GET'


# import requests
# import json
# response = requests.get("https://api.thecatapi.com/v1/breedz")

# def jsonprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=2)
#     print(text)

# print(response.reason)
