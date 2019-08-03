#from flask_sqlalchemy import Integer, Column, String
from apis import db


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

