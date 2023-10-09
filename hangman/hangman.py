import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #split as letters
    used_letters = set() #for user input
    alphabet = set(string.ascii_uppercase)
    lives = 7

    #get user input as long as the condition is true
    while len(word_letters) > 0 and lives > 0:
        
        print(f'You have {lives} left and you have used these lettrs:', ' '.join(used_letters))
        
        #current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word', ' '.join(word_list))
        
        #Logic
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')
            
        elif user_letter in used_letters:
            print('\nYou have already used the letter, please input another letter')

        else:
            print('\nInvalid letter')

    if lives == 0:
        print('No more lives left, you died.\nThe word is, ',word)
    else:
        print('YAY! You guessed the word', word, '!!') 

        
if __name__ == '__main__':
    hangman()
