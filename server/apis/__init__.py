import urllib.parse
from flask import Flask, jsonify #, url_for
from flask_cors import CORS
from extensions import db
#from flask_restplus import Api
from flask_admin import Admin
from flask_admin.contrib.sqla import  ModelView
from sqlalchemy.types import Boolean, String

from apis.users.routes import mod as users_mod
from apis.auth.routes import mod as auth_mod
from apis.main.routes import mod as main_mod
from apis.message.routes import mod as note_mod

from apis.message.models import Messages, MessageContents
from apis.auth.models import User

class UserView(ModelView):
    form_columns = ("username", "password", "color", "initials", "admin")
#    form_optional_types = (Boolean, String)
    


def create_app(config_file='../settings.py'):
    app = Flask(__name__)
    # app.config.from_object(config_by_name[env or 'test'])
    app.config.from_pyfile(config_file)
    
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};Server=tcp:hndserver.database.windows.net,1433;Database=hnd;Uid=mj@hndserver;Pwd=Hitmail1;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['SECRET_KEY'] ='mysecret'

    cors = CORS(app)
    
    app.register_blueprint(users_mod)
    app.register_blueprint(auth_mod, url_prefix='/auth')
    app.register_blueprint(main_mod)
    app.register_blueprint(note_mod) #,url_prefix='/messages')

    db.init_app(app)
    
    admin = Admin(app)

    admin.add_view(UserView(User, db.session))
    # admin.add_view(ModelView(Messages, db.session))
    # admin.add_view(ModelView(MessageContents, db.session))


    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app

# def setup_db():
#     from apis.auth.models import User
#     from apis.message.models import Message
#     db.create_all()
 

