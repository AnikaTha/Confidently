#this makes a basic web server displaying "Hello, World!"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    return "secret message!!! :O"

#if you want to run it locally through command window w/ python3 app.py
if __name__ == '__main__':
    app.run()


