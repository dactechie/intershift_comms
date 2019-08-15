from flask import Flask #, jsonify #, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handover-migrate.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handover.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"
db = SQLAlchemy(app)
from sqlalchemy.sql import func


messages_read_users = db.Table('read_messages',
                         db.Column('user_id', db.Integer, db.ForeignKey('Users.id') ),
                         db.Column('message_id', db.Integer, db.ForeignKey('Messages.id') ),
                         db.Column('read_date', db.DateTime(timezone=True), server_default=func.now())
                        )

class Users(db.Model):     
    __tablename__  = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean, default=False)
    # created_messages = db.relationship('Message', backref='user',
    #                                    lazy="dynamic", cascade="all,delete")
    read_messages = db.relationship('Messages', secondary=messages_read_users,
                                    backref=db.backref('readers', lazy='dynamic')
                                   )
    # read_messages = db.relationship('ReadMessage',backref='user',
    #                                 lazy="dynamic", cascade="all,delete")
    def __init__(self, username, password, public_id, admin):
        self.username = username
        self.password = password
        self.public_id = public_id
        self.admin = admin



class MessageContents(db.Model):
    __tablename__  = 'MessageContents'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(1000))
    message_id = db.Column(db.Integer, db.ForeignKey('Messages.id'))
    meta = db.relationship("Messages", back_populates="message_contents")
    def __init__(self, content, message_id):
        self.content = content
        self.message_id = message_id


class Messages(db.Model):
    __tablename__  = 'Messages'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    created_user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    update_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    message_contents = db.relationship('MessageContents', back_populates='meta', uselist=False,
                                        cascade="all,delete")
    def __init__(self, title, created_user_id):
        self.title = title        
        self.created_user_id = created_user_id


db.create_all()
u = Users('aftab','cool','sdfs',True)
m = Messages('title',1)
db.session.add(u)
db.session.add(m)
db.session.commit()

Messages.query.first().message_contents
mc = MessageContents('this is the content', message_id=m.id)
db.session.add(mc)
db.session.commit()

mesg_content = Messages.query.first().message_contents

messge = MessageContents.query.first().meta

# m.id
# 1
# mc.id
# 1

# class Message(db.Model):

#     __tablename__  = 'Messages'

#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(100))
#     content = db.Column(db.String(1000))
#     created_user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     update_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())

#     # read_users = db.relationship('Message', secondary=messages_read_users,
#     #                                 backref=db.backref('messages', lazy='dynamic')
#     #                                )


#     # read_users = db.relationship('ReadMessage', backref='message',
#     #                              lazy="dynamic", cascade="all,delete")


#     def __init__(self, title, content, user_id):
#         self.title = title
#         self.content = content
#         self.created_user_id = user_id
