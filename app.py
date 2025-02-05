from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load JSON data once, at startup
with open(os.path.join("data", "states.json")) as f:
    data = json.load(f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/states', methods=['GET'])
def get_states():
    states = [state["state"] for state in data["states"]]
    return jsonify(states)

@app.route('/districts/<state_name>', methods=['GET'])
def get_districts(state_name):
    state_data = next((state for state in data["states"] if state["state"] == state_name), None)
    return jsonify(state_data["districts"] if state_data else [])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

