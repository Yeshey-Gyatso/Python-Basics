from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "hello world from python"
app.run(host="0.0.0.0", port=50100, debug=True)