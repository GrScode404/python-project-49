import operator
from random import choice, randint

from brain_games.scripts.engine import run_game


# def brain_calc():
#     greet()
#     name = welcome_user()
#     count = 0
#     win_streak = 3
#     print('What is the result of the expression?')
#
#     while count < win_streak:
#
#         operations = [
#             ('+', operator.add),
#             ('-', operator.sub),
#             ('*', operator.mul)
#         ]
#
#         a = randint(1, 10)
#         b = randint(1, 10)
#         symbol, operation = choice(operations)
#
#         print(f'Question: {a} {symbol} {b}')
#         user_answer = prompt.string('Your answer: ')
#         correct_answer = operation(a, b)
#
#         if is_correct_answer(user_answer, correct_answer):
#             count += 1
#             print('Correct')
#
#         else:
#
#             print(f'"{user_answer}" is wrong answer ;(. '
#                   f'Correct answer was "{correct_answer}" ')
#             print(f"Let's try again, {name}!")
#             break
#         if count == win_streak:
#             print(f'Congratulations, {name}!')
#
def game_logic():
    operations = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]
    a = randint(1, 10)
    b = randint(1, 10)

    symbol, operation = choice(operations)

    question = f'{a} {symbol} {b}'
    correct_answer = operation(a, b)

    operation(a, b)
    return question, correct_answer


def brain_calc():
    game_rule = 'What is the result of the expression?'
    run_game(game_rule, game_logic)





