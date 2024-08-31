from os import environ

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    background_color = environ.get("BACKGROUND_COLOR", "lightblue")

    return render_template('index.html', background_color=background_color)
