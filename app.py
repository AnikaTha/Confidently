from flask import Flask, request, jsonify
import corrector
import draft_text

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    return "secret message!!! :O"

 
@app.route('/check', methods=['GET']) 
def check(): 
    val = corrector.test_confidence("amritab@vt.edu", True)
    return val

@app.route('/rewrite', methods=['GET']) 
def rewrite(): 
    val = corrector.test_confidence("amritab@vt.edu", False)
    return val

#if you want to run it locally through command window w/ python3 app.py
if __name__ == '__main__':
    app.run()


