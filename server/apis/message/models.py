from apis import db#, messages_read_users
from sqlalchemy.sql import func

messages_read_users = db.Table('read_messages',
                         db.Column('user_id', db.Integer, db.ForeignKey('Users.id') ),
                         db.Column('message_id', db.Integer, db.ForeignKey('Messages.id') ),
                         db.Column('read_date', db.DateTime(timezone=True), server_default=func.now())
                        )

class Message(db.Model):

    __tablename__  = 'Messages'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    created_user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    update_date = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # read_users = db.relationship('Message', secondary=messages_read_users,
    #                                 backref=db.backref('messages', lazy='dynamic')
    #                                )


    # read_users = db.relationship('ReadMessage', backref='message',
    #                              lazy="dynamic", cascade="all,delete")


    def __init__(self, title, content, created_user_id):
        self.title = title
        self.content = content
        self.created_user_id = created_user_id



# class ReadMessage(db.Model):

#     __tablename__  = 'ReadMessages'

#     id = db.Column(db.Integer, primary_key=True)
#     last_seen_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     message_id =  db.Column(db.Integer, db.ForeignKey('Messages.id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

#     def __init__(self, user_id, message_id):
#         self.user_id = user_id
#         self.message_id = message_id
    
#     def update_last_seen_date(self):
#         self.last_seen_date = func.now()
