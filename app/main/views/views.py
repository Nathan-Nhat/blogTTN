from flask import render_template, current_app
from app.main import main
from app import db
from app.auth.models.roles_model import permission_require
from app.auth.models.roles_model import Permission
from flask_login import current_user


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/get_config')
def config():
    return '<h1>12344556{}<h1>'.format(current_app.config['MAIL_PASSWORD'])


@main.route('/create_database')
def create_database():
    from app.auth.models.user_model import User
    from app.auth.models.roles_model import Roles
    db.create_all()
    return render_template('index.html')


@main.route('/insert_roles')
def insert_roles():
    from app.auth.models.roles_model import Roles
    role = Roles()
    role.insert_role()
    return render_template('index.html')


@main.route('/drop_database')
def drop_database():
    db.drop_all()
    return render_template('index.html')


@permission_require(Permission.ADMIN)
@main.route('/for_admin', methods=['GET'])
def admin_only():
    return '<h1> For admin only : {} </h1>'.format(current_user.username)
