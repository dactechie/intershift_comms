from flask import Blueprint, jsonify, request
from ..auth.service import token_required
from .service import UserService


mod = Blueprint('admin', __name__)


@mod.route('/admin', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    users = UserService.get_all()  #users = User.query.all()
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

    user = UserService.get_by_public_id(public_id=public_id) 
    if not user:
        return jsonify({'message':'No user found'})
    
    result = {"username":user.username,
                 "public_id":user.public_id,
                 "password":user.password,
                 "admin":user.admin} 
    return jsonify({'user': result})


@mod.route('/admin', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    data = request.get_json()
    user = UserService.create(data)

    return jsonify({'message' : f'New user creatd! public id: {user.public_id}'})


@mod.route('/admin/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    user = UserService.get_by_public_id(public_id=public_id)
    if not user:
        return jsonify({'message':'No user found'})
    
    UserService.update(user)

    return jsonify({'message': 'the user has been promoted'})


@mod.route('/admin/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})
    
    user = UserService.get_by_public_id(public_id=public_id)
    if not user:
        return jsonify({'message':'No user found'})

    UserService.delete(user)
    
    return jsonify({'message': 'the user has been deleted.'})

