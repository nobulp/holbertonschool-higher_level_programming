#!/usr/bin/python3
"""Minimal Flask API (users)."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    u = users.get(username)
    if not u:
        return jsonify(error="User not found"), 404
    return jsonify(u)


def _build_user(payload):
    return {
        "username": payload["username"],
        "name": payload.get("name", ""),
        "age": payload.get("age", 0),
        "city": payload.get("city", "")
    }


@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify(error="Invalid JSON"), 400

    payload = request.get_json()

    username = payload.get("username")
    if not username:
        return jsonify(error="Username is required"), 400

    if username in users:
        return jsonify(error="Username already exists"), 409

    users[username] = _build_user(payload)
    return jsonify(message="User added", user=users[username]), 201


if __name__ == "__main__":
    app.run()
