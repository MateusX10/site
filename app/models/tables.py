# Do módulo "app", estou importando a variável "db"
from app import db


# Cria e define a tabela "usuário" no banco de dados
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String), unique=True)
    email = db.Column(db.String), unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String)


    def __init__(self, id, name, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"



class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", foreign_keys=user_id)


    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id


    def __repr__(self):
        return f"<Post {self.id}>"



class Follow(db.Model):
    __tablename__ = "follow"


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    
    user = db.relationship("User", foreign_keys=user_id)
    follower = db.relationship("User", foreign_keys=follower_id)

