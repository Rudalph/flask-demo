from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to home page"

@app.route('/add/<int:x>')
def add(x):
    return f"sum is {x+1}"

