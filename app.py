from flask import Flask,render_template,flash, redirect, url_for
from account import Registration, Login
app = Flask(__name__)
app.config['SECRET_KEY'] = '85006f36b15fd56b8ccdcc455e8b6a04'
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