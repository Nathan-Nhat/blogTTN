import os
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager
if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
