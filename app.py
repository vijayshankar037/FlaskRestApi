#Importing packages from flask
from flask import Flask, jsonify, request, Response, json

#Initalizing app varable from Flask
#app = Flask(__name__)
from BookModel import *
from setting import *

#books collection
# books = [
#     {
#         "name":"Progamming in C",
#         "author": "Denis Rich",
#         "isbn": 12345001
#     },
#     {
#         "name":"Python3",
#         "author": "Matt",
#         "isbn":12345002
#     }
# ]

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
    books = Book.get_all_books()
    return jsonify({"books": books})

#GET book/:isbn
@app.route('/book/<int:isbn>')
def get_book_by_isbn(isbn):
    book = Book.get_book(isbn)
    if book:
        return jsonify(book)

    response = Response("", status=404, mimetype="application/json")
    return response

#POST insert book
@app.route('/book', methods = ['POST'])
def add_book():
    book_params = request.get_json()
    if validateBookObject(book_params):
        Book.add_book(book_params["name"], book_params["author"], book_params["isbn"])
        response = Response("Book Added", status=201, mimetype="application/json")
        response.headers['Location'] = "/book/" + str(book_params['isbn'])
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
    if Book.delete_book(isbn):
        response = Response("", status = 204, mimetype='application/json')
        return response

    invalidBookErrorMsg = {
        "error": "Book with isbn {} is not found, so therefore unable to delete book".format(isbn)
    }
    response = Response(json.dumps(invalidBookErrorMsg), status = 404, mimetype ="application/json")
    return response


#Start Flask service
#app.run(port =5000)
app.run()
