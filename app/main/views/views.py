from flask import render_template, current_app
from app.main import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/get_config')
def config():
    return '<h1>12344556{}<h1>'.format(current_app.config['MAIL_PASSWORD'])
