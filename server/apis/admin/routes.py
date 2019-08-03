from flask import Blueprint, jsonify, request, make_response
#import jwt
from apis.auth.models import User
from apis.auth.routes import token_required
import uuid
from werkzeug.security import generate_password_hash
from apis import app, db

mod = Blueprint('admin', __name__)

@mod.route('/admin', methods=['GET'])
@token_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    users = User.query.all()
    output = [{"username":u.username,
                 "public_id":u.public_id,
                 "password":u.password,
                 "admin":u.admin} for u in users]

    return jsonify({'users': output})

@mod.route('/admin/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message':'No user found'})
    
    result = {"username":user.username,
                 "public_id":user.public_id,
                 "password":user.password,
                 "admin":user.admin} 
    return jsonify({'user': result})


@mod.route('/admin', methods=['POST'])
#@token_required
def create_user():
    # if not current_user.admin:
    #     return jsonify({'message':'Cannot perform that function'})

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()),
                    username=data['username'],
                    password=hashed_password,
                    admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'New user creatd!'})


@mod.route('/admin/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message':'No user found'})
    user.admin = True
    db.session.commit()

    return jsonify({'message': 'the user has been promoted'})


@mod.route('/admin/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})
    
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message':'No user found'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'the user has been deleted.'})

