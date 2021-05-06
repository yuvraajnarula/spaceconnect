from spaceconnect import db , loginManager
from flask_login import UserMixin


@loginManager.user_loader

def loadUser(user_id):
    return User.query.get(int())



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='https://media.discordapp.net/attachments/741244174736556076/839414477920796702/icon.png')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
