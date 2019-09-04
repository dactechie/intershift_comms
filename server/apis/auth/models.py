from werkzeug.security import generate_password_hash
import uuid
from sqlalchemy.ext.hybrid import hybrid_property
from extensions import db
from apis.message.models import messages_read_users

class User(db.Model):     
    __tablename__  = 'Users'
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False) # @directionshealth.com
    _password = db.Column(db.String(100))
    color = db.Column(db.String(10), unique=True)
    initials = db.Column(db.String(4), unique=True)
    admin = db.Column(db.Boolean, default=False)

    @hybrid_property
    def password(self):
        """Return the hashed user password."""
        return self._password

    @password.setter
    def password(self, new_pass):
        hashed_password = generate_password_hash(new_pass, method='sha256')
        self._password = hashed_password
        if not self.public_id:
            self.public_id = str(uuid.uuid4())

    # created_messages = db.relationship('Message', backref='user',
    #                                    lazy="dynamic", cascade="all,delete")

    read_messages = db.relationship('Messages', secondary=messages_read_users,
                                    backref=db.backref('readers', lazy='dynamic')
                                   )

    # def __init__(self, username, password, public_id='', admin=False):
    #     self.username = username
    #     self.password = password
    #     self.public_id = public_id
    #     self.admin = admin