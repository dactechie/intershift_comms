from functools import wraps
import datetime
from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import check_password_hash
import jwt
from apis.auth.models import User
from apis import app


mod = Blueprint('auth', __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message':'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


def _unableToLogin():
    return make_response('Could not verify!',
                         401, 
                         {'WWW-Authenticate': 'Basic realm="Login Required"'})

@mod.route('/')
def login():
    auth  = request.authorization
    if not auth or not auth.username or not auth.password:
        return _unableToLogin()

    user = User.query.filter_by(username=auth.username).first()
    if not user:
        return _unableToLogin()

    if check_password_hash(user.password, auth.password):
        token  = jwt.encode({'public_id': user.public_id, 
                             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=120),                             
                            }, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return _unableToLogin()

# @mod.route('/logout')
# @token_required
# def logout(current_user):

#     user = User.query.filter_by(username=auth.username).first()
#     if not user:
#         return _unableToLogin()

#     if check_password_hash(user.password, auth.password):
#         token  = jwt.encode({'public_id': user.public_id, 
#                              'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=120),                             
#                             }, app.config['SECRET_KEY'])
#         return jsonify({'token': token.decode('UTF-8')})

#     return _unableToLogin()


# @mod.route('/register')
# def register():
#     username = request.json.get('username')
#     password = request.json.get('password')
#     if username is None or password is None:
#          return jsonify({'message':'Username/Password was not entered'}), 401  # missing arguments
#     if User.query.filter_by(username = username).first() is not None:
#         abort(400) # existing user
#     user = User(username = username)
#     user.hash_password(password)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({ 'username': user.username }), 201
