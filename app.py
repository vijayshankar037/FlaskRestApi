from flask import Flask, jsonify, request, Response
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

#books params validation
def validateBookObject(bookObject):
    if "name" in bookObject and "author" in bookObject and "isbn" in bookObject:
        return True
    else:
        return False

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

@app.route('/book', methods = ['POST'])
def add_book():
    book_params = request.get_json()
    if validateBookObject(book_params):
        new_book = {
        "name": book_params["name"],
        "author": book_params["author"],
        "isbn": book_params["isbn"]
        }
        books.insert(0, new_book)
        response = Response("Book Added", status=201, mimetype="application/json")
        response.headers['Location'] = "/book/" + str(new_book['isbn'])
        return response
    else:
        response = Response('Bad Request(Wrong paramets submitted): Correct parems are\n{"name":"abc", "author":"xyz", "isbn":123 }', status=400, mimetype="application/json")
        return response

#app.run(port =5000)
app.run()
