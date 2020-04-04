#Importing packages from flask
from flask import Flask, jsonify, request, Response, json

#Initalizing app varable from Flask
app = Flask(__name__)

#books collection
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

#GET /
@app.route('/')
def hello_world():
    return "Hello world"

#GET /books
@app.route('/books')
def get_books():
    return jsonify({"books": books})

#GET book/:isbn
@app.route('/book/<int:isbn>')
def get_book_by_isbn(isbn):
    for book in books:
        if book['isbn'] == isbn:
         return book

#POST insert book
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
        invalidBookErrorMsg = {
        "error":"Invalid book object passed in request",
        "helpString":'Data passed in similer to this {"name":"abc", "author":"xyz", "isbn":123 }'
        }
        response = Response( json.dumps(invalidBookErrorMsg), status=400, mimetype="application/json")
        return response

#DELETE /book/isbn
@app.route('/book/<int:isbn>', methods = ['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books.pop(i)
            response = Response("", status = 204, mimetype='application/json')
            return response
        i+=1

    invalidBookErrorMsg = {
        "error": "Book with isbn {} is not found, so therefore unable to delete book".format(isbn)
    }
    response = Response(json.dumps(invalidBookErrorMsg), status = 404, mimetype ="application/json")
    return response


#Start Flask service
#app.run(port =5000)
app.run()
