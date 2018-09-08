from app import app, login
from app import db
from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm
from app.models import User

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
     users = User.query.all()
     return render_template('users.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        flash('You are already logged in')
        # return redirect(url_for('login'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('profile'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out')
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        # sets a hashed password
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('about'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/profile')
@login_required
def profile():
    # if current_user.is_authenticated:
    #     user = current_user.username
    # user = 'N/A'
    return render_template('profile.html', title='Profile')