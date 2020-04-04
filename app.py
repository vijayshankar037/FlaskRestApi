from flask import Flask, jsonify

app = Flask(__name__)

books = [
{
	"id": 1,
	"name": "python",
	"price": 1500,
	"Number": 123456789
},
{
	"id": 2,
	"name":"Ruby",
	"price": 1600,
	"Number": 123123123

}]

@app.route('/books')
def hello():
	return jsonify({"books":books})


@app.route('/books/<int:id>')
def get_book(id):
	book_arry = {}
	for book in books:
		if book['id'] == id:
			book_arry = {
			'name': book['name'],
			'price': book['price'],
			'Number': book['Number']
			}
			return book_arry
		return "Not Found" 

if __name__=="__main__":
	app.run(debug=True)