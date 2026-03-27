#!/usr/bin/python3
"""Flask app displaying product data from JSON, CSV, or SQLite."""

import csv
import json
import os
import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json_products():
    """Read products from the JSON file."""
    file_path = os.path.join(BASE_DIR, "products.json")

    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def read_csv_products():
    """Read products from the CSV file."""
    file_path = os.path.join(BASE_DIR, "products.csv")
    products = []

    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

    return products


def read_sql_products():
    """Read products from the SQLite database."""
    file_path = os.path.join(BASE_DIR, "products.db")
    connection = sqlite3.connect(file_path)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render the contact page."""
    return render_template("contact.html")


@app.route("/items")
def items():
    """Render the items page with data loaded from JSON."""
    file_path = os.path.join(BASE_DIR, "items.json")

    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return render_template("items.html", items=data.get("items", []))


@app.route("/products")
def products():
    """Render products loaded from the requested source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            product_list = read_json_products()
        elif source == "csv":
            product_list = read_csv_products()
        elif source == "sql":
            product_list = read_sql_products()
        else:
            return render_template(
                "product_display.html",
                error="Wrong source",
                products=[],
            )
    except (OSError, json.JSONDecodeError, sqlite3.Error):
        return render_template(
            "product_display.html",
            error="Database error",
            products=[],
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )

        product_list = [
            product for product in product_list if product.get("id") == product_id
        ]

        if not product_list:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )

    return render_template("product_display.html", products=product_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
