from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    scores = db.relationship("Score", backref="user", lazy="dynamic")

    def __str__(self):
        return f"User: {self.username}"

    def get(self, username):
        return self.user[id]


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_title = db.Column(db.String(20), index=True, nullable=True)
    quiz_score = db.Column(db.Integer, index=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __str__(self):
        return f"Quiz: {self.quiz_title} = {self.quiz_score}"

    def get(self, username):
        return self.user[id]


score = Score()
user = User()