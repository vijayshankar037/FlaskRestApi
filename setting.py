from flask import Flask
app = Flask(__name__)

#database conectivity Sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/rv-singh/Desktop/python/flask/flaskrestapi/flaskApi.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False