from flask import Blueprint, render_template, redirect, request, flash, session
from flask_login import login_required, current_user
from quiz.client import get_me_question
from quiz import db
from quiz.models import User, Score

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")


@base.route("/profile/")
@login_required
def profile():
    quizzes = Score.query.all()
    return render_template("profile.html", username=current_user.username, quizzes=quizzes)


@base.route("/trivia/", methods=["GET"])
@login_required
def trivia():
    question = get_me_question()
    session["q"] = question

    return render_template("trivia.html", username=current_user.username, question=question)


@base.route("/trivia/true", methods=["GET", "POST"])
@login_required
def correct():
    username = current_user.username

    id = User.query.filter_by(username=username).first()

    quest = session.get("q", None)

    quiz = Score(
        category=quest["category"], question=quest["question"], level=quest["difficulty"], score=1, user_id=id
    )

    db.session.add(quiz)
    db.session.commit()

    return redirect("/trivia/")