from flask import Blueprint, render_template
from flask_login import login_required, current_user
from quiz.client import get_me_question
from quiz import db


base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")


@base.route("/profile/")
@login_required
def profile():
    questions = get_me_question()
    return render_template("profile.html", username=current_user.username, questions=questions)
