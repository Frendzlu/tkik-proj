import os

from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS 

app = Flask(__name__) 
CORS(app)


@app.route("/")
def hello_world():
    return render_template("main.html", message="this is from server")

@app.route("/favicon.ico")
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route("/eval_chord_code", methods=['POST'])
def eval_chord_code():
    data = request.get_json() 
    content = data.get('content')

    print(f'received: {content}')

    return jsonify({
        'message': 'skibidi',
        'data': 'not for you mr sigma'
    })