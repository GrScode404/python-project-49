import operator
from random import choice, randint

from brain_games.scripts.engine import run_game


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

    return question, correct_answer


def brain_calc():
    game_rule = 'What is the result of the expression?'
    run_game(game_rule, game_logic)