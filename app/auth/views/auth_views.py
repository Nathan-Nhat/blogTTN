from app.auth import auth
from flask import render_template, flash, redirect, url_for, request
from .auth_form import LoginForm, SignupForm, ResendForm
from flask_login import login_user, logout_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
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
        return redirect(url_for('auth.sign_up'))
    return render_template('signup.html', form=sign_up_form)


@auth.route('/logout')
def log_out():
    logout_user()  # delete current_user from session, cookie
    flash('You have been logged out.', category="danger")
    return redirect(url_for('main.index'))


@auth.route('/confirm/<username>/<token>')
def confirm_user(username, token):
    flash("Confirm successfully. Please log in again", category="success")
    return redirect(url_for('auth.login'))


@auth.route('/re_confirm', methods=['GET', 'POST'])
def resend_confirm():
    resend_confirm_form = ResendForm()
    if resend_confirm_form.validate_on_submit():
        flash('The confirmation mail is sent. Please check it!', category="success")
        return redirect(url_for('auth.login'))
    return render_template('resend.html', form=resend_confirm_form)
