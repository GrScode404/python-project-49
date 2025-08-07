from brain_games.cli import welcome_user
from brain_games.games.brain_games import greet
from brain_games.scripts.utils import ask_question, is_correct_answer


def run_game(game_rule, game_logic):
    greet()
    name = welcome_user()
    print(game_rule)
    count = 0
    win_streak = 3

    while count < win_streak:
        question, correct_answer = game_logic()
        user_answer = ask_question(question)
        if is_correct_answer(user_answer, correct_answer):
            count += 1
            print('Correct')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}" ')
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')