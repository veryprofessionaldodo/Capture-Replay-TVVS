from flask import Flask, render_template, url_for
import socket

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)