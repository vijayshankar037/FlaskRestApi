from flask import Flask,json
import jwt
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'FLASK_API'

#database conectivity Sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/rv-singh/Desktop/python/flask/flaskrestapi/flaskApi.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False