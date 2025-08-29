from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

flats = []
next_id = 1

@app.route("/")
def index():
    return jsonify({"message": "Flask backend is running"})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route("/flats", methods=["GET"])
def get_flats():
    return jsonify(flats)

@app.route("/flats", methods=["POST"])
def add_flat():
    global next_id
    data = request.json
    flat = {
        "id": next_id,
        "type": data.get("type", "1BHK"),
        "price": data.get("price", 0),
        "location": data.get("location", "")
    }
    flats.append(flat)
    next_id += 1
    return jsonify(flat), 201

@app.route("/flats/<int:flat_id>", methods=["DELETE"])
def delete_flat(flat_id):
    global flats
    flats = [f for f in flats if f["id"] != flat_id]
    return jsonify({"message": "Flat deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
