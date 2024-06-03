from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to home page"

@app.route('/add/<int:x>')
def add(x):
    return f"sum is {x+1}"

if __name__== "__main__":
    app.run(debug=True, port=5000)