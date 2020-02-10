import random
import string


adjectives = ['sleepy', 'slow', 'smelly',
            'wet', 'fat', 'red',
            'orange', 'yellow', 'green',
            'blue', 'purple', 'fluffy',
            'white', 'proud', 'brave']


nouns =     ['apple', 'dinosaur', 'ball',
            'toaster', 'goat', 'dragon',
            'hammer', 'duck', 'panda']


color =     ['red', 'blue', 'green',
            'yellow', 'orange', 'purple',
            'white','black','gray']


print('Welcome to Password Picker!')



while True:
    
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        # you can introduce this to the password string to make it more complex
        color = random.choice(color)

        number = random.randrange(0, 100)

        special_char = random.choice(string.punctuation)


        password = adjective + noun + str(number) + special_char
        print('Your new password is: %s' % password)
    
    
    response = input('Would you like another password? Type y or n: ')
    
    
    if response == 'n':
        break