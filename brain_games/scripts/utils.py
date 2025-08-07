import prompt


def ask_question(question):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer


def is_correct_answer(user_answer, correct_answer):
    return str(user_answer).lower() == str(correct_answer).lower()


