from flask import Flask, jsonify, request, Response
from setting import *
# app = Flask(__name__)

books = [
{
	"id": 1,
	"name": "python",
	"price": 1500,
	"number": 123456789
},
{
	"id": 2,
	"name":"Ruby",
	"price": 1600,
	"number": 123123123

},
{
	"id": 3,
	"name": "A",
	"price": 1500,
	"number": 123456789
},
{
	"id": 4,
	"name":"B",
	"price": 1600,
	"number": 123123123

},
{
	"id": 5,
	"name": "C",
	"price": 1500,
	"number": 123456789
},
{
	"id": 6,
	"name":"D",
	"price": 1600,
	"number": 123123123

}]


@app.route('/books', methods=['POST', 'GET'])
def hello():
	if request.method == 'GET':
		return jsonify({"books":books})
	elif request.method == "POST":
		book_param = request.get_json()
		new_book = {
		"id": book_param['id'],
		"name": book_param['name'],
		"price": book_param['price'],
		"number": book_param['number'] 
		}
		# if new_book['id'] == book_param['id']:
		books.insert(0, new_book)
		response = Response("", status=200, mimetype='application/json')
		return response
	response = Response("", status=404, mimetype='application/json')
	return response


@app.route('/books/<int:id>')
def get_book(id):
	book_arry = {}
	for book in books:
		if book['id'] == id:
			book_arry = {
			'name': book['name'],
			'price': book['price'],
			'number': book['number']
			}
			return book_arry
		return "Not Found" 



@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
	response = request.get_json()
	# return response
	for book in books:
		if book['id'] == id:
			book.update(response)
			response = Response("", status=200)
			return response
	# response.headers['location'] = "/books/" + str(id)
	return "Not Found"


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
	i = 0;
	for book in books:
		if book['id'] == id:
			books.pop(i)
			response = Response("", status=204, mimetype='application/json')
			return response
		i += 1
	response = Response("", status=404, mimetype='application/json')
	return response



if __name__=="__main__":
	app.run(debug=True)