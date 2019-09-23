

from flask import Blueprint, jsonify, request, make_response
from apis.users.service import get_by_username
from .service import get_token_ifok, token_required
import json

mod = Blueprint('auth', __name__)

def _unableToLogin():
    return make_response('Could not verify!',
                         401, 
                         {'WWW-Authenticate': 'Basic realm="Login Required"'})

@mod.route('/login', methods=['POST'])
def login():
    auth = None
    username = None
    if request.data:
        auth = json.loads(request.data.decode('utf-8'))
    else:
        auth = request.authorization    # for Postman
    username = auth['username']
   
    if not username or not auth['password']:
        return _unableToLogin()

    user = get_by_username(username)
    if not user:
        return _unableToLogin()
    
    decoded_token = get_token_ifok(user, auth['password'])
    if decoded_token:
        u = {
            'username' : user.username,
            'initials': user.initials,
            'public_id': user.public_id,
            'admin': user.admin,
            'color':user.color
        }
        return jsonify({'token': decoded_token, 'user': u})

    return _unableToLogin()


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
