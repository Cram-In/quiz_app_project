from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from config import Config


class ScoreBoard(FlaskForm):
    points = IntegerField("Points", validators=[DataRequired()])
    win = StringField("True", validators=[DataRequired()])
    loos = StringField("False", validators=[DataRequired()])
