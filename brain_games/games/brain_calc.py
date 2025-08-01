import operator
from random import choice, randint

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.utils import is_correct_answer


def calc():
    name = welcome_user()
    count = 0
    win_streak = 3
    print('What is the result of the expression?')

    while count < win_streak:

        operations = [
            ('+', operator.add),
            ('-', operator.sub),
            ('*', operator.mul)
        ]

        a = randint(1, 100)
        b = randint(1, 100)
        symbol, operation = choice(operations)

        print(f'Question: {a} {symbol} {b}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = operation(a, b)

        if is_correct_answer(user_answer, correct_answer):
            count += 1
            print('Correct')

        else:

            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}" ')
            print(f"Let's try again, {name}!")
            break
        if count == win_streak:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':

    calc()






