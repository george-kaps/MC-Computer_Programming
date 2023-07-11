from app import db

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.String (100), primary_key_=True)
    username =db.Column(db.String (100), unqiue=True, nullable=False)
    password =db.Column(db.String(255), nullable=False)
    email =db.Column(db.String(100), unqiue=True, nullable=False)