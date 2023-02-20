from flask import Flask, jsonify, abort, request
import json
import os
import tempfile

app = Flask(__name__)

storage_path = '/opt/flask/storage.data'
with open(str(storage_path), "r") as f:
    keys = json.load(f)


@app.route('/api/v1/storage/json/all', methods=['GET'])
def get_keys():
    return jsonify({'keys': keys})


@app.route('/api/v1/storage/json/read/key=<key_id>', methods=['GET'])
def get_key(key_id):
    if len(key_id) == 0:
        abort(404)
    return jsonify({key_id: keys[key_id]})


@app.route('/api/v1/storage/json/write', methods=['POST'])
def create_key():
    key = request.get_json()
    keys.update(key)
    return key, 201


if __name__ == '__main__':
    app.run(debug=True)
