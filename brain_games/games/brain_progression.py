from random import randint

from brain_games.scripts.engine import run_game


def generate_progression():
    start = randint(1, 100)
    step = randint(1, 10)
    progression = []
    progression_length = 10

    for index in range(progression_length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def game_logic():
    progression = generate_progression()
    answer_index = randint(0, len(progression) - 1)
    correct_answer = progression[answer_index]

    question_list = progression.copy()
    question_list[answer_index] = '..'

    question = " ".join(str(num) for num in question_list)

    return question, correct_answer


def brain_progression():
    game_rule = 'What number is missing in the progression?'
    run_game(game_rule, game_logic)