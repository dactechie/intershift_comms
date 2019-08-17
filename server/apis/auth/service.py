

import datetime
from werkzeug.security import check_password_hash
import jwt  #pyjwt
from functools import wraps
from flask import jsonify, request, current_app as app
from .models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        bearer_token = request.headers.environ.get('HTTP_AUTHORIZATION')
        if bearer_token:
            token = bearer_token.split(' ')[1]
        if not token:
            return jsonify({'message':'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message':'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated



def get_token_ifok(user:User, auth_password:str):

    if check_password_hash(user.password, auth_password):            
        token  = jwt.encode({'public_id': user.public_id, 
                            'exp': datetime.datetime.utcnow() +
                                    datetime.timedelta(seconds=app.config['TOKEN_EXPIRATION_SECONDS']),
                            }, app.config['SECRET_KEY'])

        return token.decode('UTF-8')
    else: 
        return None
