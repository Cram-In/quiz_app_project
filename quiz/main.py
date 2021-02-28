from flask import Blueprint, render_template, redirect, request, flash, session
from flask_login import login_required, current_user
from quiz.client import get_me_question
from quiz import db
from quiz.models import User, Score
from quiz.utilities import check_answers

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")


@base.route("/profile/")
@login_required
def profile():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    scores = Score.query.filter_by(user_id=user.id).all()

    return render_template("profile.html", username=username, scores=scores)


@base.route("/trivia/", methods=["GET"])
@login_required
def trivia():
    question = get_me_question()
    session["q"] = question

    return render_template("trivia.html", username=current_user.username, question=question)


@base.route("/trivia/check/", methods=["POST"])
@login_required
def correct():
    username = current_user.username

    user = User.query.filter_by(username=username).first()

    quest = session.get("q", None)
    print(f"<=====correct=====>")
    if request.form["True"] == "True":
        print(f"<======= if request True========>")
        answers = "True"
        print(answers)
        check_answers(answers, quest, user)
    else:
        print(f"<======= if request False========>")
        answers = "False"
        check_answers(answers, quest, user)

    return redirect("/trivia/")