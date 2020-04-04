from flask import Flask, jsonify

app = Flask(__name__)

books = [
{
	"name": "python",
	"price": 1500,
	"Number": 123456789
},
{
	"name":"Ruby",
	"price": 1600,
	"Number": 123123123

}]

@app.route('/books')
def hello():
	return jsonify({"books":books})

app.run(port=5001)