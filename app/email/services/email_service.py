from app import mail
from flask_mail import Message
from flask import render_template
from threading import Thread
from flask import current_app


def __send_async_email(app_instance, msg):
    with app_instance.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['BLOG_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['BLOG_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    th = Thread(target=__send_async_email, args=[app, msg])
    th.start()
