from apis import db #, messages_read_users
from sqlalchemy.sql import func


messages_read_users = db.Table('read_messages',
                         db.Column('user_id', db.Integer, db.ForeignKey('Users.id') ),
                         db.Column('message_id', db.Integer, db.ForeignKey('Messages.id') ),
                         db.Column('read_date', db.DateTime(timezone=True), server_default=func.now())
                        )

class User(db.Model):
     
    __tablename__  = 'Users'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean, default=False)

    # created_messages = db.relationship('Message', backref='user',
    #                                    lazy="dynamic", cascade="all,delete")

    read_messages = db.relationship('Message', secondary=messages_read_users,
                                    backref=db.backref('readers', lazy='dynamic')
                                   )

    # read_messages = db.relationship('ReadMessage',backref='user',
    #                                 lazy="dynamic", cascade="all,delete")

    def __init__(self, username, password, public_id, admin):
        self.username = username
        self.password = password
        self.public_id = public_id
        self.admin = admin

