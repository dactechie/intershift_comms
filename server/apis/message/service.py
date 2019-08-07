from extensions import db
from typing import List
from sqlalchemy import desc
from apis.auth.models import User
from .models import Message
#from .interface import MessageInterface

class MessageService():

    @staticmethod
    def set_reader(message: Message, user: User):
        message.readers.append(user)
        db.session.commit()


    @staticmethod
    def get_all() -> List[Message]:
        messages = Message.query.order_by(desc(Message.creation_date)).all()
        return [{ "id": message.id,
                "title": message.title,
                "content": message.content,
                #"created_user_id": message.created_user_id,
                "read_by": [user.username for user in message.readers.all()]
                } 
                for message in messages]


    @staticmethod
    def get_by_id(message_id: int) -> Message:
        return Message.query.get(message_id)


    @staticmethod
    def update(changes: dict, message: Message) -> Message:
        message.title = changes['title']
        message.content=changes['content']
        message.created_user_id=changes['created_user_id'] # warning it overrides the original author
        db.session.commit()
        return message


    @staticmethod
    def delete(message: Message) -> int:
        db.session.delete(message)
        db.session.commit()
        return message.id


    @staticmethod
    def create(changes: dict, created_by_user: any) -> Message:

        new_message = Message(title=changes['title'],
                                content=changes['content'],
                                created_user_id=created_by_user.id)
        new_message.readers.append(created_by_user)

        db.session.add(new_message)
        db.session.commit()

        return new_message
