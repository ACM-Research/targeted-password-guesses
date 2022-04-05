from flask import Flask, render_template, send_from_directory, request
import json
import passwords

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", theme=request.cookies.get("theme") or "system")


@app.route("/guess", methods=["POST"])
def guess():
    return json.dumps(passwords.guess())


@app.route("/styles/<path:path>")
def send_css(path):
    return send_from_directory("static/styles", path)

@app.route("/scripts/<path:path>")
def send_scripts(path):
    return send_from_directory("static/scripts", path)

@app.route("/fonts/<path:path>")
def send_fonts(path):
    return send_from_directory("static/fonts", path)
