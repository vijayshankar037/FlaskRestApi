from flask import Flask, jsonify, request
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

@app.route('/book/<int:isbn>')
def get_book_by_isbn(isbn):
    for book in books:
        if book['isbn'] == isbn:
         return book

@app.route('/books', methods = ['POST'])
def add_book():
    return jsonify(request.get_json())

#app.run(port =5000)
app.run()
