# app.py
from flask import Flask
print("2325")
app = Flask(__name__)

@app.route("/")
def hello_World():
    print("2325")
    return "Hello World!"