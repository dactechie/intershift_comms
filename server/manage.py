from apis import db, app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apis.auth.models import User
from apis.message.models import Message

migrate = Migrate(app,db)

manager = Manager(app)

manager.add_command('db', MigrateCommand) # pthion mamage.py db ....

if __name__ == '__main__':
    manager.run()




