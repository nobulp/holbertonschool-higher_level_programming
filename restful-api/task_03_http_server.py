#!/usr/bin/python3
"""
task_03_http_server.py
A simple API using Python's http.server module.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for a very small JSON API."""

    def _send_text(self, status_code, message):
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code, payload):
        body_str = json.dumps(payload)
        body = body_str.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests and route endpoints."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_json(
                200,
                {"version": "1.0", "description": "A simple API built with http.server"},
            )
        else:
            self._send_text(404, "Endpoint not found")

    def log_message(self, format, *args):
        """Silence default logging (optional)."""
        return


def run_server(host="0.0.0.0", port=8000):
    """Start the HTTP server."""
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()
