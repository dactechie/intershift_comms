from flask import Flask #, jsonify #, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handover.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"

db = SQLAlchemy(app)


class User(db.Model):
     
    __tablename__  = 'Users'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean, default=False)
    messages = db.relationship('Message', backref='user',
                               lazy="dynamic", cascade="all,delete")

    def __init__(self, username, password, public_id, admin):
        self.username = username
        self.password = password
        self.public_id = public_id
        self.admin = admin


class Message(db.Model):

    __tablename__  = 'Messages'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

db.create_all()
