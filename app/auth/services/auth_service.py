from app.auth.models.user_model import User
from sqlalchemy.exc import IntegrityError
from app import db
from app.email.services.email_service import send_mail
from app.auth.models.user_model import generate_confirmation_token


def sign_up_user(user: User) -> bool:
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return False
    return True


def send_mail_confirm(user: User):
    token = generate_confirmation_token(user)
    send_mail(user.email, "Register Account", "new_user", user=user, token=token)
