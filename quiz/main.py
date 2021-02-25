from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from quiz.client import get_me_question
from quiz import db
from quiz.models import score, user

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")

@base.route("/profile/")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)

@base.route("/trivia/")
@login_required
def trivia():
    question = get_me_question()
    return render_template("trivia.html", username=current_user.username, question=question)

@base.route("/counter/<username>", methods=["POST"])
@login_required
def counter(username):
    question = get_me_question()
    user_id = user.get(username)
    if request.method == "POST":
        quiz = Score(request.form["category"], request.form["score"], request.form["user_id"])

        db.session.add(quiz)
        db.session.commit()

    
    return render_template("trivia.html", username=current_user.username, question=question)