from flask import render_template, url_for
from panlab import app


@app.route("/")
def index():
    response = render_template("index.html")
    return response, 200


@app.route("/posts")
def posts():
    response = render_template("posts.html")
    return response, 200


@app.route("/tools")
def tools():
    response = render_template("tools.html")
    return response, 200

