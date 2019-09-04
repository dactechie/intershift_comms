
from extensions import db
from typing import List
from sqlalchemy import desc
import uuid
from werkzeug.security import generate_password_hash
from apis.auth.models import User



def get_by_id(user_id: int) -> User:
    user = User.query.get(user_id)
    return user


def get_by_public_id(public_id: int) -> User:
    user = User.query.filter_by(public_id=public_id).first()
    return user


def get_by_username(username: str)-> User:
    return User.query.filter_by(username=username).first()


def get_all() -> List[User]:
    users = User.query.all() # order_by(desc(User.creation_date))
    return users


def update(user: User) -> User:
    user.admin=True
    db.session.commit()
    return user


def create(data: dict) -> User:
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()),
                    username=data['username'],
                    password=hashed_password,
                    admin=False)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def delete(user: User) -> int:
    db.session.delete(user)
    db.session.commit()
    return user.id