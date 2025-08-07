from random import randint

from brain_games.scripts.engine import run_game


def is_even(number):
    return number % 2 == 0


# def brain_even():
#     greet()
#     name = welcome_user()
#     count = 0
#     win_streak = 3
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#
#     while count < win_streak:
#         current_number = randint(1, 100)
#         print(f'Question: {current_number}')
#         user_answer = prompt.string('Your answer: ')
#         correct_answer = 'yes' if is_even(current_number) else 'no'
#
#         if user_answer == correct_answer:
#             count += 1
#             print('Correct')
#
#         else:
#             print(f'"{user_answer}" is wrong answer ;(. '
#                   f'Correct answer was "{correct_answer}" ')
#             print(f"Let's try again, {name}!")
#             break
#
#     if count == win_streak:
#         print(f'Congratulations, {name}!')

def game_logic():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def brain_even():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(game_rule, game_logic)