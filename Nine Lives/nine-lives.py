import random

def update_clue(guess_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guess_letter == secret_word[index]:
            clue[index] = guess_letter
            unknown_letters = unknown_letters - 1
            
        index = index+1
    return unknown_letters

def set_difficulty(num):
    global lives
    lives = 12 - ((num-1)*3)


lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt',
        'otter', 'plane', 'brush', 'horse', 'light']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False
unknown_letters = len(secret_word)
difficulty = input('Choose difficulty (type 1, 2, or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)

set_difficulty(difficulty)


while lives > 0:
    print(clue)
    print('Lives left: ' + (heart_symbol * lives))
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1
    if unknown_letters == 0:
        guessed_word_correctly = True
        break
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
