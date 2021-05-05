from flask import Flask,render_template,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from account import Registration, Login
app = Flask(__name__)
app.config['SECRET_KEY'] = '85006f36b15fd56b8ccdcc455e8b6a04'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='https://media.discordapp.net/attachments/741244174736556076/839414477920796702/icon.png')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
@app.route('/')
def about():
    return render_template('about.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)
@app.route('/register', methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}. ', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)
if __name__ == "__main__":
    app.run(debug=True)