from random import randint

from brain_games.scripts.engine import run_game


def is_prime(number):
    num_of_dividers = 1
    for divider in range(2, number + 1):
        if number % divider == 0:
            num_of_dividers += 1

    return num_of_dividers <= 2


def game_logic():
    num = randint(1, 100)
    question = f'{num}'
    correct_answer = "yes" if is_prime(num) else "no"

    return question, correct_answer


def brain_prime():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(game_rule, game_logic)