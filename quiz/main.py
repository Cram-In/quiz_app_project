from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

base = Blueprint("base", __name__)


@base.route("/")
def index():
    return render_template("index.html")


@base.route("/profile/")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)
