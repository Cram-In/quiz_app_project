from pytrivia import Category, Diffculty, Type, Trivia



def get_me_question():
    trivia_client = Trivia(True)
    question = (trivia_client.request(1, Category.Books , Diffculty.Easy, Type.True_False))
    print(question)
    return question
