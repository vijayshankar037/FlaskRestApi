from flask import Flask, jsonify, request, Response
from setting import *
from models import *

@app.route('/books', methods=['POST', 'GET'])
def hello():
	if request.method == 'GET':
		books = Book.get_all_books()
		return jsonify({"books":books})
	elif request.method == "POST":
		book_param = request.get_json()
		new_book = {
		"id": book_param['id'],
		"name": book_param['name'],
		"price": book_param['price'],
		"number": book_param['number'] 
		}
		books.insert(0, new_book)
		response = Response("", status=200, mimetype='application/json')
		return response
	response = Response("", status=404, mimetype='application/json')
	return response


@app.route('/books/<int:num>')
def get_book_number(num):
	number = Book.get_book(num)
	return jsonify({"number":number})

@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
	request_book = request.get_json()	
	book_update = Book.update_book_name(id, request_book['name'])
	return jsonify({"book_update": book_update})
	

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):	
	if Book.delete_book(id):
		response = Response("", status=204, mimetype='application/json')
		return response

	response = Response("", status=404, mimetype='application/json')
	return response

if __name__=="__main__":
	app.run(debug=True)