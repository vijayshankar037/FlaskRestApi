from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from setting import app

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books' #table name with schema details
    id = db.Column(db.Integer, primary_key=True) #table field id as PK
    name = db.Column(db.String(80), nullable=False) #table field name
    author = db.Column(db.String(80), nullable=False) #table field author
    isbn = db.Column(db.Integer) #table field isbn

    # def __init__(**kwargs):
    #     super(Foo, self).__init__(**kwargs)

    def json(self):
        return {
            'name': self.name,
            'author': self.author,
            'isbn': self.isbn
        }

    #Model method to insert new record in db
    def add_book(_name, _author, _isbn):
        new_book = Book(name= _name, author= _author, isbn = _isbn)
        db.session.add(new_book)
        db.session.commit()

    #Model method to fetch all records
    def get_all_books():
        return [
            Book.json(book) for book in Book.query.all()
        ]

    #Get book with isbn
    def get_book(_isbn):
        book = Book.query.filter_by(isbn=_isbn).first()
        if book:
            return Book.json(book)

        return False

    #Delete book with isbn
    def delete_book(_isbn):
        is_success = Book.query.filter_by(isbn=_isbn).delete()
        db.session.commit()
        return bool(is_success)

    #Defining representation of Model object
    def __repr__(self):
        book_object = {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'isbn': self.isbn
        }
        return json.dumps(book_object)
