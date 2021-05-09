from flask import render_template, url_for, flash, redirect, request
from spaceconnect import app, db, bcrypt
from spaceconnect.forms import RegistrationForm, LoginForm ,ApplyForm
from spaceconnect.models import User, Apply
from flask_login import login_user, current_user, logout_user, login_required
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='Mission')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/apply", methods=['GET', 'POST'])
@login_required
def apply():
    form = ApplyForm()
    if form.validate_on_submit():
        apply = Apply(fullname = form.fullname.data, age = form.age.data, content = form.content.data, email = current_user)
        db.session.add(apply)
        db.session.commit()
        flash('Your application submitted successfully!')
        return redirect(url_for('home'))
    return render_template('apply.html', title='Apply',form=form)
@app.route('/admin')
def admin():
    candidates = Apply.query.all()

    return render_template('admin.html', title='Admin', candidates=candidates)