from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATBASE_URI'] = "sqlite:///Users/vijay/workspace/python/FlaskRestApi/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
