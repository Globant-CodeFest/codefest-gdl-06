from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/resultsEvaluation', methods=['GET'])
def resultsEvaluation():
    with open('resultsEvaluation.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/timeComparison', methods=['GET'])
def timeComparison():
    with open('timeComparison.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/clustersWithSimilarBehavior', methods=['GET'])
def clustersWithSimilarBehavior():
    with open('clustersWithSimilarBehavior.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run()