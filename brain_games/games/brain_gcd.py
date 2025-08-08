from random import randint

from brain_games.scripts.engine import run_game


def game_logic():

    a = randint(1, 100)
    b = randint(1, 100)

    question = f'{a} {b}'
    correct_answer = 0

    while b != 0:
        a, b = b, a % b
        if b == 0:
            correct_answer = a

    return question, correct_answer


def brain_gcd():
    game_rule = 'Find the greatest common divisor of given numbers.'
    run_game(game_rule, game_logic)