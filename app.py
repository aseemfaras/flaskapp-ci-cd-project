from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Initialize data as None
data = None

try:
    # Load JSON data once, at startup
    data_file = os.path.join(os.path.dirname(__file__), "data", "states.json")
    with open(data_file) as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: states.json file not found in {os.path.join('data')}")
    data = {"states": []}
except json.JSONDecodeError:
    print("Error: Invalid JSON format in states.json")
    data = {"states": []}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/states', methods=['GET'])
def get_states():
    if not data:
        return jsonify([]), 500
    states = [state["state"] for state in data["states"]]
    return jsonify(states)

@app.route('/districts/<state_name>', methods=['GET'])
def get_districts(state_name):
    if not data:
        return jsonify([]), 500
    try:
        state_data = next((state for state in data["states"] if state["state"] == state_name), None)
        if state_data is None:
            return jsonify({"error": f"State '{state_name}' not found"}), 404
        return jsonify(state_data["districts"])
    except KeyError:
        return jsonify({"error": "Invalid data format"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

