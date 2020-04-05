from flask import Flask 
import json 
from flask_sqlalchemy import SQLAlchemy
from setting import app

db = SQLAlchemy(app)

# New Book Model create
class Book(db.Model):
	__tablename__ = "books"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False)
	price = db.Column(db.Float, nullable=False)
	number = db.Column(db.Integer)

	def json(self):
		return {
			"id": self.id,
			"name": self.name,
		 	"price": self.price,
		 	"number": self.number
		  }


	# New Record add 
	def add_book(_name,_price, _number):
		new_book = Book(name=_name, price=_price, number=_number)
		db.session.add(new_book)
		db.session.commit()

	# Model Fetch all Data
	def get_all_books():
		# return Book.query.all()
		return [Book.json(book) for book in Book.query.all()]
	
	# Filter one record in model
	def get_book(_number):
		return Book.json(Book.query.filter_by(number=_number).first())
	# Delete one record
	def delete_book(_id):
		is_deleted = Book.query.filter_by(id=_id).delete()
		db.session.commit()
		return bool(is_deleted)


	# Model get id Record update
	def update_book_name(_id, _name):
		update_book = Book.query.filter_by(id=_id).first()
		update_book.name = _name
		is_updated = db.session.commit()
		return bool(is_updated)
		
	#Reprasent all record
	def __repr__(self):
		book_object = {
		'id': self.id,
		'name': self.name,
		'price': self.price,
		'number': self.number
		}
		return json.dumps(book_object)