""" Authenticating blueprint routes and view function. """

from flask import render_template, redirect, request, url_for, flash
from . import auth 
from .forms import LoginForm
from flask_login import login_user, logout_user, login_required
from ..models import User

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))