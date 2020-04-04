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


	# New Record add 
	def add_book(_name,_price, _number):
		new_book = Book(name=_name, price=_price, number=_number)
		db.session.add(new_book)
		db.session.commit()

	# Model Fetch all Data
	def get_all_books():
		return Book.query.all()
	
	# Filter one record in model
	def get_book(_number):
		return Book.query.filter_by(number=_number).first()

	# Model get id then delete record
	def delete_book(id):
		row = Book.query.get(id)
		db.session.delete(row)
		db.session.commit()

	# # Model get id Record update
	# def update_book(id):
	# 	update = Book.query.get(id)
	# 	update.name = name
	# 	update.price = price
	# 	update.number = number
	# 	db.session.commit()
		
	#Reprasent all record
	def __repr__(self):
		book_object = {
		'id': self.id,
		'name': self.name,
		'price': self.price,
		'number': self.number
		}
		return json.dumps(book_object)