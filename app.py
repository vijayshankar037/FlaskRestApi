from flask import Flask, jsonify, request, Response, json
app = Flask(__name__)
books = [
    {
        'name':'book1',
        'price':30,
        'id':1
    },
    {
        'name':'book2',
        'price':60,
        'id':2
    }
]

def validateObject(new_object):
	if ('name' in new_object and 'price' in new_object and 'id' in new_object):
		return True
	else:
		return False

@app.route('/books')
def get_books():
	return jsonify({'books': books})

@app.route('/books',methods=['POST'])
def create_book():
	response_object = request.get_json()
	if validateObject(response_object):
		new_response = {
			"id": response_object['id'],
			"name": response_object['name'],
			"price": response_object['price']
		}

		books.insert(0, new_response)
		response = Response('',201,mimetype='application/json')
		response.headers['Location'] = '/book/' + str(new_response["id"])
		return response
	else:
		invalidBookOjectErrorMsg = {
			'error':'invalid object params'
		}
		response = Response(json.dumps(invalidBookOjectErrorMsg),status=400,mimetype='application/json')
		return response


@app.route('/book/<int:id>', methods=['PUT'])
def replace_object(id):
	response_data = request.get_json()
	new_object = {
		'id': id,
		'name': response_data['name'],
		'price': response_data['price']
	}
	i=0;
	for book in books:
		if book['id'] == id:
			books[i] = new_object

		i += 1;

	response = Response('',status=204)
	response.headers['Location'] = '/book/' + str(id)
	return response

@app.route('/book/<int:id>')
def get_book(id):
    return_value = {}
    for book in books:
        if book['id'] == id:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
    return  jsonify(return_value)

@app.route('/book/<int:id>',methods=['PATCH'])
def update_object(id):
	response_data = request.get_json()
	new_object = {}
	if 'name' in response_data:
		new_object ={
			'name': response_data['name']
		}
	if 'price' in response_data:
		new_object ={
			'price': response_data['price']
		}
	for book in books:
		if book['id'] == id:
			book.update(new_object)
			response = Response('',status=204)
			response.headers['Location'] = '/book/' + str(id)
			return response

app.run()