from extensions import db
from typing import List
from sqlalchemy import desc
from apis.auth.models import User
from .models import Messages, MessageContents
#from .interface import MessageInterface


def set_reader(message: Messages, user: User):
    message.readers.append(user)
    db.session.commit()

# TODO : Add : get-all between dates


def get_all() -> List[object]:
    messages = Messages.query.order_by(desc(Messages.created_date)).all()
    users = User.query.all()

    return [{ "id": message.id,
            "title": message.title,
            "created_date": message.created_date,
            "created_username": [user.username for user in users if user.id == message.created_user_id],
            "read_by": [user.username for user in message.readers.all()]
            } 
            for message in messages]


def get_by_id(message_id: int) -> Messages:
    return Messages.query.get(message_id)


def update(changes: dict, message: Messages) -> Messages:
    message.title = changes['title']
    message.message_contents.content = changes['content']
    message.created_user_id = changes['created_user_id'] # warning it overrides the original author
    db.session.commit()
    return message


def delete(message: Messages) -> int:
    db.session.delete(message)
    db.session.commit()
    return message.id


def create(mesg_dict: dict, created_by_user: any) -> Messages:

    new_message = Messages(title=mesg_dict['title'],                                
                            created_user_id=created_by_user.id)
    new_message.readers.append(created_by_user)

    db.session.add(new_message)
    db.session.commit()

    mc = MessageContents(mesg_dict['content'], message_id=new_message.id)
    db.session.add(mc)
    db.session.commit()
    
    return new_message
