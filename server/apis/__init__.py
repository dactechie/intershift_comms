from flask import Flask, jsonify #, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#from flask_restplus import Api

app = Flask(__name__)
cors = CORS(app)
#CORS(app, resources=r'/api/*')


#app.config.from_pyfile('app_config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handover.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"

db = SQLAlchemy(app)


from apis.admin.routes import mod as admin_mod
from apis.auth.routes import mod as auth_mod
from apis.main.routes import mod as main_mod
from apis.message.routes import mod as note_mod

app.register_blueprint(admin_mod)
app.register_blueprint(auth_mod, url_prefix='/auth')
app.register_blueprint(main_mod)
app.register_blueprint(note_mod) #,url_prefix='/messages')

# def setup_db():
#     from apis.auth.models import User
#     from apis.message.models import Message
#     db.create_all()



# def create_app(env=None):
#     from app.config import config_by_name
#     from app.routes import register_routes

#     app = Flask(__name__)
#     app.config.from_object(config_by_name[env or 'test'])
#     api = Api(app, title='Flaskerific API', version='0.1.0')

#     register_routes(api, app)
#     db.init_app(app)

#     @app.route('/health')
#     def health():
#         return jsonify('healthy')
#     return app