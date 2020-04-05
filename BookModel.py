from flask import Flask,json
from flask_sqlalchemy import SQLAlchemy
from setting import app

db = SQLAlchemy(app)

class Book(db.Model):
	#creating table into database
	__tablename__ = "books"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80),nullable=False)
	price = db.Column(db.Float,nullable=False)

	#creating recode into db
	def add_book(_name,_price):
		new_book = Book(name=_name,price=_price)
		db.session.add(new_book)
		db.session.commit()

	#get all record
	def get_all_books():
		return Book.query.all()

	def __repr__(self):
		book_object ={
			'id': self.id,
			'name': self.name,
			'price': self.price
		}
		return json.dumps(book_object)
		