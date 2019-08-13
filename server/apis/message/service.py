from extensions import db
from typing import List
from sqlalchemy import desc
from apis.auth.models import User
from .models import Messages, MessageContents
#from .interface import MessageInterface

class MessageService():

    @staticmethod
    def set_reader(message: Messages, user: User):
        message.readers.append(user)
        db.session.commit()


    @staticmethod
    def get_all() -> List[object]:
        messages = Messages.query.order_by(desc(Messages.creation_date)).all()
        return [{ "id": message.id,
                "title": message.title,
                "creation_date": message.creation_date,
                "created_user_id": message.created_user_id,
                "read_by": [user.username for user in message.readers.all()]
                } 
                for message in messages]


    @staticmethod
    def get_by_id(message_id: int) -> Messages:
        return Messages.query.get(message_id)


    @staticmethod
    def update(changes: dict, message: Messages) -> Messages:
        message.title = changes['title']
        message.message_contents.content = changes['content']
        message.created_user_id = changes['created_user_id'] # warning it overrides the original author
        db.session.commit()
        return message


    @staticmethod
    def delete(message: Messages) -> int:
        db.session.delete(message)
        db.session.commit()
        return message.id


    @staticmethod
    def create(changes: dict, created_by_user: any) -> int:

        new_message = Messages(title=changes['title'],                                
                                created_user_id=created_by_user.id)
        new_message.readers.append(created_by_user)

        db.session.add(new_message)
        db.session.commit()

        mc = MessageContents(changes['content'], message_id=new_message.id)
        db.session.add(mc)
        db.session.commit()
        
        return new_message.id
