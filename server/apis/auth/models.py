from apis import db

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

