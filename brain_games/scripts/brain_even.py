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
        print(user_answer)

        if is_even(current_number) and user_answer == 'yes':
            count += 1
            print('Correct!')
        elif not is_even(current_number) and user_answer == 'no':
            count += 1
            print('Correct!')

        else:
            if user_answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")

            if user_answer == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")

            if user_answer != 'yes' and user_answer != 'no':

                if is_even(current_number):
                    print(f"'{user_answer}' is wrong answer ;(. "
                          f"Correct answer was 'yes'.")

                else:
                    print(f"'{user_answer}' is wrong answer ;(. "
                          f"Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__brain_even__':
    brain_even()