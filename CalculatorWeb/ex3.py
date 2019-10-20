from flask import Flask, render_template, url_for
import socket
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('calculator3.html')

if __name__ == '__main__':
    app.run(debug=False, port=int(os.getenv('PORT', 1111)))