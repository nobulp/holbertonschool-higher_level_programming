#!/usr/bin/python3
"""
task_02_requests.py
Fetch and process posts from JSONPlaceholder.
"""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print status code + all titles."""
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title", ""))


def fetch_and_save_posts():
    """Fetch posts and save id/title/body into posts.csv."""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()
        data = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
