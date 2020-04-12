import os
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager, Server
if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    manager = Manager(app)
    server = Server(host='0.0.0.0', port=5000)
    manager.add_command('db', MigrateCommand)
    manager.add_command('runserver', server)
    manager.run()
