from flask import Blueprint, render_template, redirect, request, flash
from flask_login import login_required, current_user
from quiz.client import get_me_question
from quiz import db
from quiz.models import score, user
from quiz.forms import ScoreBoard

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")


@base.route("/profile/")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)


@base.route("/trivia/", methods=["GET", "POST"])
@login_required
def trivia():
    question = get_me_question()
    return render_template("trivia.html", username=current_user.username, question=question)


"""
form = ScoreBoard
    scor = 0
    if request.method == "POST":
        form.request["win"]
        form.request["loos"]
        if question["correct_answer"] == form.request["win"]:
            scor += 1
            flash("You are correct")
            quiz = Score(request.form["category"], request.form["score"], request.form["user_id"])

            db.session.add(quiz)
            db.session.commit()
            return redirect("/trivia/")
        else:
            flash("You are incorrect")
            quiz = Score(request.form["category"], request.form["score"], request.form["user_id"])

            db.session.add(quiz)
            db.session.commit()
"""