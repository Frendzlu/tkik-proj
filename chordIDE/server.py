import os

from flask import Flask
from flask import send_from_directory, render_template


app = Flask(__name__) 

@app.route("/")
def hello_world():
    return render_template("main.html", message="this is from server")

@app.route("/favicon.ico")
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
