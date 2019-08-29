from flask import Blueprint, jsonify, request, make_response
from apis.auth.service import token_required
from apis.admin.service import get_by_id as get_user
from extensions import db
from .service import (set_reader, get_all, get_by_id,
                 delete, create, update)
from .models import Messages

mod = Blueprint('messages', __name__)


@mod.route('/messages', methods=['GET'])
@token_required
def get_all_messages(current_user):
    output = get_all()

    for m in output:
        m['read_by_me'] = current_user.username in m['read_by']        
        actioned_by_uid = m.get('actioned_by')
        if actioned_by_uid:
            m["actioned_by"] = get_user(actioned_by_uid).username

    return jsonify({'messages': output})


@mod.route('/messages/<message_id>', methods=['GET'])
@token_required
def get_one_message(current_user, message_id):

    message:Messages = get_by_id(message_id=message_id)
    if not message:
        return jsonify({'message':'No message found'})
        
    if current_user in message.readers:
        #TODO update the last read time
        pass
    else:
        set_reader(message, current_user)

    created_user = get_user(message.created_user_id)

    result = {"title":message.title,
              "content":message.message_contents.content,
              "created_username": created_user.username,  
              "id": message.id,
              "created_date": message.created_date}
                  
    if message.actioned_by:
        result["actioned_by"] = get_user(message.actioned_by).username
        print("actioned by " + result["actioned_by"] )
    elif message.with_action:        
        result["with_action"] = message.with_action

    return jsonify({'message': result})


@mod.route('/messages', methods=['POST'])
@token_required
def create_message(current_user):
    data = request.get_json()
    message = create(
                    {'title': data['title'],
                    'content': data['content'],
                    'with_action': data.get('with_action'),
                    },
                    created_by_user=current_user)

    created_user = get_user(message.created_user_id)
    result = {"title":message.title,
              "created_username": created_user.username,
              "id": message.id,
              "created_date": message.created_date,
              "with_action": message.with_action,
              "read_by":  created_user.username,
              "read_by_me": True,
              }
    return jsonify({'message': result}), 201


@mod.route('/messages/<message_id>', methods=['PUT'])
@token_required
def edit_message(current_user, message_id):
    # if not current_user.admin:
    #     return jsonify({'message':'Cannot perform that function'})
    
    message = get_by_id(message_id=message_id)
    if not message:
        return jsonify({'message':'No message found'})
    
    data = request.get_json()

    response = update(current_user, data, message)

    return jsonify(response)


@mod.route('/messages/<message_id>', methods=['DELETE'])
@token_required
def delete_message(current_user, message_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})

    message = get_by_id(message_id=message_id)    
    if not message:
        return jsonify({'message':'No message found'})

    delete(message)

    return jsonify({'message': 'the message has been deleted.'}), 204



