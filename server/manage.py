import os
from  apis import db, create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = create_app(config_file=os.path.abspath('./settings.py'))

migrate = Migrate(app,db)

manager = Manager(app)

manager.add_command('db', MigrateCommand) # pthion mamage.py db ....


from apis.auth.models import User
from apis.message.models import  messages_read_users, MessageContents, Messages

if __name__ == '__main__':
    manager.run()




