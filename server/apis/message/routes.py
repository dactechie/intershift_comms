from flask import Blueprint, jsonify, request, make_response
from apis.auth.service import token_required
from extensions import db
from .service import MessageService

mod = Blueprint('messages', __name__)


@mod.route('/messages', methods=['GET'])
@token_required
def get_all_messages(current_user):
    output = MessageService.get_all()
    return jsonify({'messages': output})


@mod.route('/messages/<message_id>', methods=['GET'])
@token_required
def get_one_message(current_user, message_id):
    message = MessageService.get_by_id(message_id=message_id)
    if not message:
        return jsonify({'message':'No message found'})
        
    if current_user in message.readers:
        #TODO update the last read time
        pass
    else:
        MessageService.set_reader(message, current_user)

    result = {"title":message.title,
              "content":message.content,
              "created_user_id": message.created_user_id}

    return jsonify({'message': result})


@mod.route('/messages', methods=['POST'])
@token_required
def create_message(current_user):
    data = request.get_json()
    new_message = MessageService.create(
                    {'title': data['title'],'content': data['content']},
                    created_by_user=current_user)
    
    return jsonify({'message' : 'New message created!'})


@mod.route('/messages/<message_id>', methods=['PUT'])
@token_required
def edit_message(current_user, message_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    message = MessageService.get_by_id(message_id=message_id)
    if not message:
        return jsonify({'message':'No message found'})
    
    data = request.get_json()
    message = MessageService.update({'title': data['title'],
                                    'content': data['content'],
                                    'created_user_id':current_user.id},
                                    message)
  
    return jsonify({'message': 'the message has been edited'})


@mod.route('/messages/<message_id>', methods=['DELETE'])
@token_required
def delete_message(current_user, message_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})
    
    message =  MessageService.get_by_id(message_id=message_id)
    
    if not message:
        return jsonify({'message':'No message found'})

    MessageService.delete(message)

    return jsonify({'message': 'the message has been deleted.'})



