from random import randint

from brain_games.scripts.engine import run_game


def is_even(number):
    return number % 2 == 0


def game_logic():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def brain_even():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(game_rule, game_logic)