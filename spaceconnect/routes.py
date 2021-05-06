from flask import Flask,render_template,flash, redirect, url_for
from spaceconnect import app,db,bcrypt
from spaceconnect.account import Registration, Login
from spaceconnect.model import User
from flask_login import login_user, current_user, logout_user
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password ,form.password.data):
            login_user(user,remember=form.remember_me.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)
@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data , email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. ', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))