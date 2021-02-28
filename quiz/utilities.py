from flask import request, session, flash, redirect
from quiz.models import Score
from quiz import db


def check_answers(answers, quest, user):
    print("<=================checker=====================>")
    print(f"my answer", answers)

    print(f"correct_answer", quest["correct_answer"])
    if answers == quest["correct_answer"]:

        quiz = Score(
            category=quest["category"], question=quest["question"], level=quest["difficulty"], score=1, user_id=user.id
        )

        db.session.add(quiz)
        db.session.commit()
        flash("Well done! You got it wright!")

    else:

        quiz = Score(
            category=quest["category"], question=quest["question"], level=quest["difficulty"], score=0, user_id=user.id
        )

        db.session.add(quiz)
        db.session.commit()
        flash("Bad luck! Maybe next time?")