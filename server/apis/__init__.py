from flask import Flask, jsonify #, url_for
from flask_cors import CORS
from extensions import db
#from flask_restplus import Api


from apis.admin.routes import mod as admin_mod
from apis.auth.routes import mod as auth_mod
from apis.main.routes import mod as main_mod
from apis.message.routes import mod as note_mod


def create_app(config_file='../settings.py'):
    app = Flask(__name__)
    # app.config.from_object(config_by_name[env or 'test'])
    app.config.from_pyfile(config_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handover.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    cors = CORS(app)
    
    app.register_blueprint(admin_mod)
    app.register_blueprint(auth_mod, url_prefix='/auth')
    app.register_blueprint(main_mod)
    app.register_blueprint(note_mod) #,url_prefix='/messages')

    db.init_app(app)

    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app

# def setup_db():
#     from apis.auth.models import User
#     from apis.message.models import Message
#     db.create_all()
 

