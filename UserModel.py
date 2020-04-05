from setting import *

db = SQLAlchemy(app)

class User(db.Model):
	__tablename__= 'users'
	id = db.Column(db.Integer,primary_key=True)
	user_name = db.Column(db.String(90),nullable=False,unique=True)
	password = db.Column(db.String(90),nullable=False)


	#get record in json 
	def json(self):
		return {'user_name': self.user_name}

	#get user
	def get_user(_id):
		user = User.query.filter_by(id=_id).first()
		if user:
			return User.json(user)

		return False
	
	#check user is exist? 
	def user_exist(_user_name,_password):
		user = User.query.filter_by(user_name=_user_name).filter_by(password=_password).first()
		if user:
			return True

		return False

	#get all users
	def get_all_users():
		return [User.json(user) for user in User.query.all()]

	#create new user
	def create_user(_user_name,_password):
		new_user = User(user_name=_user_name,password=_password)
		db.session.add(new_user)
		db.session.commit()

	def __repr__(self):
		return {
			'user_name': self.user_name,
			'password': self.password
		}