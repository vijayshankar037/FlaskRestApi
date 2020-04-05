from setting import *

db = SQLAlchemy(app)

class Book(db.Model):
	#creating table into database
	__tablename__ = "books"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80),nullable=False)
	price = db.Column(db.Float,nullable=False)

	#send data in json
	def json(self):
		return {
			'id': self.id,
			'name': self.name,
			'price': self.price
		}

	#creating recode into db
	def create_book(_name,_price):
		new_book = Book(name=_name,price=_price)
		db.session.add(new_book)
		db.session.commit()
		return Book.json(new_book)

	#get single record
	def get_book(_id):
		book = Book.query.filter_by(id=_id).first()
		if book:
			return Book.json(book)
		return False

	#destroy book
	def destroy(_id):
		book = Book.query.filter_by(id=_id).delete()
		db.session.commit()
		return bool(book)

	#get all record
	def get_all_books():
		return [Book.json(book) for book in Book.query.all()]

	#update record price
	def update_book_price(_id,_price):
		book = Book.query.filter_by(id=_id).first()
		book.price = _price
		db.session.commit()

	#update record name
	def update_book_name(_id,_name):
		book = Book.query.filter_by(id=_id).first()
		book.name = _name
		db.session.commit()

	#replace all record 
	def replace_book(_id,_name,_price):
		book = Book.query.filter_by(id=_id).first()
		book.name = _name
		book.price = _price
		db.session.commit()

	def __repr__(self):
		book_object ={
			'id': self.id,
			'name': self.name,
			'price': self.price
		}
		return json.dumps(book_object)
	