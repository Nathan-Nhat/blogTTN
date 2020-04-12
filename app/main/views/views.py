from flask import render_template, current_app
from app.main import main
from app import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/get_config')
def config():
    return '<h1>12344556{}<h1>'.format(current_app.config['MAIL_PASSWORD'])


@main.route('/create_database')
def create_database():
    db.create_all()
    return render_template('index.html')


@main.route('/drop_database')
def drop_database():
    db.drop_all()
    return render_template('index.html')
