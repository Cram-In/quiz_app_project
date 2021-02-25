from pytrivia import Category, Diffculty, Type, Trivia

"""
https://opentdb.com/api.php?amount=1&type=multiple
"""


def get_me_question():
    trivia_client = Trivia(True)
    return trivia_client.request(1, Category.Books ,Diffculty.Easy, Type.Multiple)