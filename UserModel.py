from flask_sqlalchemy import SQLAlchemy

from setting import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            'username': self.username,
            'password': self.password

        }

    def match(_username, _password):
        user = User.query.filter_by(username=_username).filter_by(password=_password).first()
        if user is None:
            return True
        else:
            return False

    def add_user(_username, _password):
        user = User(username=_username, password=_password)
        db.session.add(user)
        db.session.commit()

    def get_users():
        return [
            User.json(user) for user in User.query.all()
        ]

    def __repr__():
        return str({
            'username':self.username,
            'password':self.password,
        })
