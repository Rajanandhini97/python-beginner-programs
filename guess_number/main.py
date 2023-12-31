import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess the random number between 1 and {x}: '))
        if guess < random_number:
            print('Nope the number is low, guess again')
        elif guess > random_number:
            print('Nope the number is high, guess again')

    print(f'Yes, you have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is this number {guess} too high (h) or too low (l), or correct (c): ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yes, computer guessed the number {guess} correctly!!')

computer_guess(10)