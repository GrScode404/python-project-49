from random import randint

import prompt

from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def brain_even():
    name = welcome_user()
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    while count < 3:
        current_number = randint(1, 100)
        print(f'Question: {current_number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(current_number) else 'no'

        if user_answer == correct_answer:
            count += 1
            print('Correct')

        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}" ')
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':

    brain_even()