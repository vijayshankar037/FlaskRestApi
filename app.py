from flask import Flask, jsonify, request, Response, json

from setting import *
from BookModel import *
from UserModel import *

#app = Flask(__name__)

#static data for testing..
# books = [
#     {
#         'name':'book1',
#         'price':30,
#         'id':1
#     },
#     {
#         'name':'book2',
#         'price':60,
#         'id':2
#     }
# ]


#login user authontication
@app.route('/login')
def get_token():
	request_data = request.get_json()
	username = str(request_data['username'])
	password = str(request_data['password'])

	match = User.user_exist(username,password)
	if match:
		date_day = datetime.datetime.utcnow()
		date_time = datetime.timedelta(seconds=1000)
		expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=1000)
		token = jwt.encode({'exp':expiration_date},app.config['SECRET_KEY'],algorithm='HS256')
		return jsonify({'token': token, 'exp_date': expiration_date})
	else:
		return Response("",401,mimetype='application/json')

def validateObject(new_object):
	if ('name' in new_object and 'price' in new_object):
		return True
	else:
		return False

#get all recodes
@app.route('/books')
def get_books():
	token = request.headers.get('token')
	try:
		jwt.decode(token,app.config['SECRET_KEY'])
	except Exception as e:
		return jsonify({'error': 'Need a valid token to view this page'}),401
	
	return jsonify({'books': Book.get_all_books()})

#creating recode api
@app.route('/books',methods=['POST'])
def create_book():
	response_object = request.get_json()
	if validateObject(response_object):
		book = Book.create_book(response_object['name'],response_object['price'])
		response = Response('',201,mimetype='application/json')
		response.headers['Location'] = '/book/' + str(book["id"])
		return response
	else:
		invalidBookOjectErrorMsg = {
			'error':'invalid object params'
		}
		response = Response(json.dumps(invalidBookOjectErrorMsg),status=400,mimetype='application/json')
		return response


#replacing hole recode with new params
@app.route('/book/<int:id>', methods=['PUT'])
def replace_object(id):
	response_data = request.get_json()
	Book.replace_book(id,response_data['name'],response_data['price'])
	response = Response('',status=204)
	response.headers['Location'] = '/book/' + str(id)
	return response

#show single recde Api
@app.route('/book/<int:id>')
def get_book(id):
	book = Book.get_book(id)
	if book:
		return jsonify(book)

	invalidBookOjectErrorMsg = {
		"error": "this Id={} Record Not Found".format(id)
	}
	response = Response(json.dumps(invalidBookOjectErrorMsg),status=404,mimetype='application/json')
	return response 

#patch or update a single attribure api
@app.route('/book/<int:id>',methods=['PATCH'])
def update_object(id):
	response_data = request.get_json()
	if 'name' in response_data:
		Book.update_book_name(id,response_data['name'])
	if 'price' in response_data:
		Book.update_book_price(id,response_data['price'])

	response = Response('',status=204)
	response.headers['Location'] = '/book/' + str(id)
	return response

#Destroy recode frome the db api
@app.route('/book/<int:id>',methods=["DELETE"])
def delete_object(id):
	if Book.destroy(id):
		response = Response('',status=204)
		response.headers['Location'] = '/books'
		return response
	invalidBookOjectErrorMsg =  {
		"error": "this Id=-{} is not present in DB".format(id)
	}
	response = Response(json.dumps(invalidBookOjectErrorMsg),status=404,mimetype='application/json')
	return response

#use to run a python server
#default port=5000, change port by prot=7000
app.run()