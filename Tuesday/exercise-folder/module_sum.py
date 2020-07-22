# Handles main adding function
from random import randint
guessed_number = randint(0, 100)

my_list = [n for n in range(1, 101)]
print(my_list)


def guessNumber(value):
    # print(value)
    # while value in my_list:
    #     print(value)
    guess = int(value)
    while guess != guessed_number:
        if guess > guessed_number:
            print('A little less')
        elif guess < guessed_number:
            print('A little more')
        elif guess == guessed_number:
            print('Huzzah, you\'ve got it!')
            break


attempt_guessed_number = input('Guess a number: ')
guessNumber(attempt_guessed_number)
