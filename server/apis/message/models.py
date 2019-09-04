from extensions import db#, messages_read_users
from sqlalchemy.sql import func

messages_read_users = db.Table('read_messages',
                         db.Column('user_id', db.Integer, db.ForeignKey('Users.id') ),
                         db.Column('message_id', db.Integer, db.ForeignKey('Messages.id') ),
                         db.Column('read_date', db.DateTime(timezone=False), server_default=func.now())
                        )

class MessageContents(db.Model):
    __tablename__  = 'MessageContents'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(2000))
    message_id = db.Column(db.Integer, db.ForeignKey('Messages.id'))
    meta = db.relationship("Messages", back_populates="message_contents")
    def __init__(self, content, message_id):
        self.content = content
        self.message_id = message_id


class Messages(db.Model):
    __tablename__  = 'Messages'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    with_action = db.Column(db.Boolean, unique=False, default=False)
    created_user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    actioned_by = db.Column(db.Integer, db.ForeignKey('Users.id'))
    actioned_date = db.Column(db.DateTime(timezone=False))
    created_date = db.Column(db.DateTime(timezone=False), server_default=func.now())
    update_date = db.Column(db.DateTime(timezone=False), onupdate=func.now())
    message_contents = db.relationship('MessageContents', back_populates='meta', uselist=False,
                                        cascade="all,delete")
    def __init__(self, title, created_user_id, with_action=False):
        self.title = title        
        self.created_user_id = created_user_id
        self.with_action = with_action



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
