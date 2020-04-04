from flask import Flask, jsonify
app = Flask(__name__)

books = [
    {
        "name":"Progamming in C",
        "author": "Denis Rich",
        "isbn": 12345001
    },
    {
        "name":"Python3",
        "author": "Matt",
        "isbn":12345002
    }
]

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/books')
def get_books():
    return jsonify({"books": books})

app.run(port =5000)
