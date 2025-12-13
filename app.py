from flask import Flask

app = Flask(__name__)

def static_function():
    return "ERR"

@app.route("/")
def hello_world():
    return "Hello, Flask! Error with test"

@app.route("/test")
def hello_world2():
    return "<h1>Hello, World -  test!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
