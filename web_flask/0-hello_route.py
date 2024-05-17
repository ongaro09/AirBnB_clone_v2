#!/usr/bin/python3
"""A script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")

print(" * Serving Flask app '0-hello_route' (lazy loading)")

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """Return a given string"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

