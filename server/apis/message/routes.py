from flask import Blueprint, jsonify, request, make_response
from apis.message.models import Message
from apis.auth.routes import token_required
from apis import db
mod = Blueprint('messages', __name__)


@mod.route('/messages', methods=['GET'])
#@token_required
def get_all_messages():#current_user):

    messages = Message.query.all()
    output = [{ "id": message.id,
                "title": message.title,
                "content": message.content,
                "created_user_id": message.created_user_id} 
             for message in messages]

    return jsonify({'messages': output})


@mod.route('/messages/<message_id>', methods=['GET'])
@token_required
def get_one_message(current_user, message_id):

    message = Message.query.filter_by(id=message_id).first()

    if not message:
        return jsonify({'message':'No message found'})
    
    
    if current_user in message.readers:
        #TODO update the last read time
        pass
    else:
        message.readers.append(current_user)        
        db.session.commit()

    result = {"title":message.title,
              "content":message.content,
              "created_user_id": message.created_user_id} 

    return jsonify({'message': result})


@mod.route('/messages', methods=['POST'])
# @token_required
def create_message(): #current_user):

    data = request.get_json()

    new_message = Message(title=data['title'],
                    content=data['content'],
                    created_user_id= 1) #current_user.id)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message' : 'New message created!'})


@mod.route('/messages/<message_id>', methods=['PUT'])
@token_required
def edit_message(current_user, message_id):
    # if not current_user.admin:
    #     return jsonify({'message':'Cannot perform that function'})

    message = Message.query.filter_by(id=message_id).first()
    if not message:
        return jsonify({'message':'No message found'})
    
    data = request.get_json()
    message.title = data['title']
    message.content=data['content']
    message.created_user_id=current_user.id  # warning it overrides the original author

    db.session.commit()

    return jsonify({'message': 'the message has been edited'})


@mod.route('/messages/<message_id>', methods=['DELETE'])
@token_required
def delete_message(current_user, message_id):
    if not current_user.admin:
        return jsonify({'message':'Cannot perform that function'})
    
    #message = Message.query.filter_by(id=message_id,
    #                                  user_id=current_user.id).first()
    message = Message.query.filter_by(id=message_id).first()
    
    if not message:
        return jsonify({'message':'No message found'})

    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'the message has been deleted.'})



