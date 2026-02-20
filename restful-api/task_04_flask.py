#!/usr/bin/python3
"""
Simple Flask API with user management.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: Don't add test data here (checker warning)
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    payload = request.get_json()

    if "username" not in payload:
        return jsonify({"error": "Username is required"}), 400

    username = payload["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": payload.get("name", ""),
        "age": payload.get("age", 0),
        "city": payload.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
