from flask import Blueprint
#from app.main.models import 

mod = Blueprint('main', __name__)

@mod.route('/')
def home():
    return '{"result": "you are on the homepage"}'
