from app.auth import auth
from flask import render_template, flash, redirect, url_for, request
from .auth_form import LoginForm, SignupForm, ResendForm
from app.auth.models.user_model import User
from flask_login import login_user, logout_user
from app.auth.services.auth_service import sign_up_user, send_mail_confirm
from app.auth.models.user_model import confirm
from app import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            if not user.confirmed:
                flash("You don't active your account yet. Please verify it via email", category="danger")
                return redirect(url_for('auth.login', form=login_form))
            login_user(user, login_form.remember_me.data)
            next = request.args.get('next')
            if next is None or next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid user name or password', category="danger")
    return render_template('login.html', form=login_form)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignupForm()
    if sign_up_form.validate_on_submit():
        user = User(username=sign_up_form.username.data,
                    password=sign_up_form.password.data,
                    email=sign_up_form.email.data)
        if not sign_up_user(user):
            flash("There an error while sign up. Please try again later", category="danger")
            return redirect(url_for('auth.sign_up'))
        send_mail_confirm(user)
        flash("Sign up success fully. An email will be sent to {}. Please check it out".format(sign_up_form.email.data),
              category="success")
        return redirect(url_for('auth.sign_up'))
    return render_template('signup.html', form=sign_up_form)


@auth.route('/logout')
def log_out():
    logout_user()  # delete current_user from session, cookie
    flash('You have been logged out.', category="danger")
    return redirect(url_for('main.index'))


@auth.route('/confirm/<username>/<token>')
def confirm_user(username, token):
    user = User.query.filter_by(username=username).first()
    if user.confirmed:
        flash("Your account have been already confirmed! Please login", category="success")
        return redirect(url_for('auth.login'))
    if user is None or not confirm(user, token):
        flash("Invalid Confirm. Please try again or click resend", category="danger")
        return redirect(url_for('auth.login'))
    db.session.commit()
    flash("Confirm successfully. Please log in again", category="success")
    return redirect(url_for('auth.login'))


@auth.route('/re_confirm', methods=['GET', 'POST'])
def resend_confirm():
    resend_confirm_form = ResendForm()
    if resend_confirm_form.validate_on_submit():
        user = User.query.filter_by(email=resend_confirm_form.email.data).first()
        if user is None:
            flash('This email {} is not registered yet. Please fill correct your email'.format(
                resend_confirm_form.email.data), category="danger")
            return redirect(url_for('auth.resend_confirm'))
        if user.confirmed:
            flash('Your account has already confirmed. Please login', category="danger")
            return redirect(url_for('auth.login'))
        send_mail_confirm(user)
        flash('The confirmation mail is sent. Please check it!', category="success")
        return redirect(url_for('auth.login'))
    return render_template('resend.html', form=resend_confirm_form)
