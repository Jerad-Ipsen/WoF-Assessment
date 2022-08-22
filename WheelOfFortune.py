from random import randint
from threading import Timer
import config

my_api_key = getattr(config, 'some_super_sensitive_key?', 'no_key_found')
my_username = getattr(config, 'python_assessment', 'no_username_found')
my_password = getattr(config, 'sft67hgy', 'no_password_found')

# Round Banks:

global player_one_rb
global player_two_rb
global player_three_rb

player_one_rb = 0
player_two_rb = 0
player_three_rb = 0

players_rb = [player_one_rb, player_two_rb, player_three_rb]

# Total Banks:

global player_one_tb
global player_two_tb
global player_three_tb

player_one_tb = 0
player_two_tb = 0
player_three_tb = 0

players_tb = [player_one_tb, player_two_tb, player_three_tb]

# Setting up , rewards, vowels, and word list/reading file:

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

reward = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 'Lose a Turn', 'Bankrupt']

words = []

file = open('words.txt','r')
for word in file:
    word_strip = word.strip()
    words.append(word_strip)
file.close()

# Introduce Game:

print('\nWelcome to the Wheel of Fortune!')

# Naming Contestants (capitalizes and checks for letters only):

print('Let\'s get the FIRST names of our contestants.')

while True:
    player_one = input('\nWho is player one? ')
    if player_one.isalpha() == False:
        print('\nUse a name with letters only')
    else:
        player_one = player_one.capitalize()
        print(f'\n{player_one} is player one!')
    break

while True:
    player_two = input('\nWho is player two? ')
    if player_two.isalpha() == False:
        print('\nUse a name with letters only')
    else:
        player_two = player_two.capitalize()
        print(f'\n{player_two} is player two!')
    break

while True:
    player_three = input('\nWho is player three? ')
    if player_three.isalpha() == False:
        print('\nUse a name with letters only')
    else:
        player_three = player_three.capitalize()
        print(f'\n{player_three} is player three!')
    break

players = [player_one, player_two, player_three]

# First Round:

int_one = randint(0,len(words)-1)
word_one = words[int_one]
word_one_empty = '_' * len(word_one)
print('\nLet\'s get our first word:')
guessed_letters = []

round_one = False

while not round_one:
    for i in range(1,4):
        if round_one == True:
            break
        else:
            print(f'{word_one_empty}')
            spin = input(f'\nGo ahead {players[i-1]}, spin the wheel! (spin) ')
            spin = randint(0,18)
            outcome = reward[spin]
            if outcome == 'Lose a Turn':
                print('\nToo bad, you lost your turn!')
            elif outcome == 'Bankrupt':
                players_rb[i-1] = 0
                print('\nOh no, you went bankrupt!')
            else:
                potential_reward = outcome
                print(f'\nYou landed on ${outcome}')
                choosing = False
                while not choosing:
                    if players_rb[i-1] >= 250:
                        try:
                            choice = int(input('\nWould you like to\n1. guess a letter?\n2. guess the word?\n3. buy a vowel?\n(1,2,3) '))
                            if choice not in range(1,4):
                                print('\nPlease choose one of the given options')
                            else:
                                choosing = True
                        except ValueError:
                            print('\nPlease choose one of the given options')
                    else:
                        try:
                            choice = int(input('\nWould you like to\n1. guess a letter?\n2. guess the word\n(1,2) '))
                            if choice not in range(1,3):
                                print('\nPlease choose one of the given options')
                            else:
                                choosing = True
                        except ValueError:
                            print('\nPlease choose one of the given options')
                if choice == 1:
                    alpha = False
                    while not alpha:
                        guess = input('\nPlease guess a letter: ')
                        if guess.isalpha() == False:
                            print('\nYou can only guess letters')
                        elif guess in vowels:
                            print('\nYou can\'t guess vowels')
                        elif guess in guessed_letters:
                            print('\nGuess a letter that has not already been guessed')
                        elif guess not in word_one:
                            print(f'\n{guess} is not in the word')
                            guessed_letters.append(guess)
                            alpha = True
                        else:
                            print(f'\nCorrect! {guess} is in the word.')
                            guessed_letters.append(guess)
                            players_rb[i-1] = players_rb[i-1] + potential_reward
                            print(f'{players[i-1]} now has ${players_rb[i-1]}')
                            #
                            word_list_one = list(word_one_empty)
                            indices = [i for i, letter in enumerate(word_one) if letter == guess]
                            for index in indices:
                                word_list_one[index] = guess
                            word_one_empty = ''.join(word_list_one)
                            if '_' not in word_one_empty:
                                round_one = True
                            #
                            alpha = True
                elif choice == 2:
                    alpha = False
                    while not alpha:
                        guess = input('\nGo ahead and guess the word: ')
                        if guess.isalpha() == False:
                            print('\nPlease guess a word')
                        elif guess != word_one:
                            print('\nI\'m sorry but that is not the word')
                            alpha = True
                        else:
                            print(f'\nCorrect! {word_one} is the word')
                            players_rb[i-1] = players_rb[i-1] + potential_reward
                            players_tb[i-1] = players_tb[i-1] + players_rb[i-1]
                            round_one = True
                            alpha = True
                else:
                    alpha = False
                    while not alpha:
                        vowel = input('\nChoose a vowel to buy: ')
                        if vowel.isalpha() == False:
                            print('\nPlease choose a vowel')
                        elif vowel not in vowels:
                            print('\nPlease choose a vowel')
                        elif vowel in guessed_letters:
                            print('\nChoose a vowel that has not been chosen')
                        elif vowel not in word_one:
                            print(f'\n{vowel} is not in the word')
                            guessed_letters.append(vowel)
                            players_rb[i-1] = players_rb[i-1] - 250
                            alpha = True
                        else:
                            print(f'\nWe do have an {vowel}')
                            players_rb[i-1] = players_rb[i-1] - 250
                            #
                            word_list_one = list(word_one_empty)
                            indices = [i for i, letter in enumerate(word_one) if letter == vowel]
                            for index in indices:
                                word_list_one[index] = vowel
                            word_one_empty = ''.join(word_list_one)
                            if '_' not in word_one_empty:
                                round_one = True
                            #
                            alpha = True

print('With round one complete, let\'s see our totals!')

print('\ntotal:')
print(f'{player_one} has ${players_tb[0]}')
print(f'{player_two} has ${players_tb[1]}')
print(f'{player_three} has ${players_tb[2]}')

# Resetting Round Banks

players_rb[0] = 0
players_rb[1] = 0
players_rb[2] = 0

# Second Round:

print('\nLet\'s begin round two')

int_two = randint(0,len(words)-1)
word_two = words[int_two]
word_two_empty = '_' * len(word_two)
print('\nLet\'s get our next word:')
guessed_letters = []

round_two = False

while not round_two:
    for i in range(1,4):
        if round_two == True:
            break
        else:
            print(f'{word_two_empty}')
            spin = input(f'\nGo ahead {players[i-1]}, spin the wheel! (spin) ')
            spin = randint(0,18)
            outcome = reward[spin]
            if outcome == 'Lose a Turn':
                print('\nToo bad, you lost your turn!')
            elif outcome == 'Bankrupt':
                players_rb[i-1] = 0
                print('\nOh no, you went bankrupt!')
            else:
                potential_reward = outcome
                print(f'\nYou landed on ${outcome}')
                choosing = False
                while not choosing:
                    if players_rb[i-1] >= 250:
                        try:
                            choice = int(input('\nWould you like to\n1. guess a letter?\n2. guess the word?\n3. buy a vowel?\n(1,2,3) '))
                            if choice not in range(1,4):
                                print('\nPlease choose one of the given options')
                            else:
                                choosing = True
                        except ValueError:
                            print('\nPlease choose one of the given options')
                    else:
                        try:
                            choice = int(input('\nWould you like to\n1. guess a letter?\n2. guess the word\n(1,2) '))
                            if choice not in range(1,3):
                                print('\nPlease choose one of the given options')
                            else:
                                choosing = True
                        except ValueError:
                            print('\nPlease choose one of the given options')
                if choice == 1:
                    alpha = False
                    while not alpha:
                        guess = input('\nPlease guess a letter: ')
                        if guess.isalpha() == False:
                            print('\nYou can only guess letters')
                        elif guess in vowels:
                            print('\nYou can\'t guess vowels')
                        elif guess in guessed_letters:
                            print('\nGuess a letter that has not already been guessed')
                        elif guess not in word_two:
                            print(f'\n{guess} is not in the word')
                            guessed_letters.append(guess)
                            alpha = True
                        else:
                            print(f'\nCorrect! {guess} is in the word.')
                            guessed_letters.append(guess)
                            players_rb[i-1] = players_rb[i-1] + potential_reward
                            print(f'{players[i-1]} now has ${players_rb[i-1]}')
                            #
                            word_list_two = list(word_two_empty)
                            indices = [i for i, letter in enumerate(word_two) if letter == guess]
                            for index in indices:
                                word_list_two[index] = guess
                            word_two_empty = ''.join(word_list_two)
                            if '_' not in word_two_empty:
                                round_two = True
                            #
                            alpha = True
                elif choice == 2:
                    alpha = False
                    while not alpha:
                        guess = input('\nGo ahead and guess the word: ')
                        if guess.isalpha() == False:
                            print('\nPlease guess a word')
                        elif guess != word_two:
                            print('\nI\'m sorry but that is not the word')
                            alpha = True
                        else:
                            print(f'\nCorrect! {word_two} is the word')
                            players_rb[i-1] = players_rb[i-1] + potential_reward
                            players_tb[i-1] = players_tb[i-1] + players_rb[i-1]
                            round_two = True
                            alpha = True
                else:
                    alpha = False
                    while not alpha:
                        vowel = input('\nChoose a vowel to buy: ')
                        if vowel.isalpha() == False:
                            print('\nPlease choose a vowel')
                        elif vowel not in vowels:
                            print('\nPlease choose a vowel')
                        elif vowel in guessed_letters:
                            print('\nChoose a vowel that has not been chosen')
                        elif vowel not in word_two:
                            print(f'\n{vowel} is not in the word')
                            guessed_letters.append(vowel)
                            players_rb[i-1] = players_rb[i-1] - 250
                            alpha = True
                        else:
                            print(f'\nWe do have an {vowel}')
                            players_rb[i-1] = players_rb[i-1] - 250
                            #
                            word_list_two = list(word_two_empty)
                            indices = [i for i, letter in enumerate(word_two) if letter == vowel]
                            for index in indices:
                                word_list_two[index] = vowel
                            word_two_empty = ''.join(word_list_two)
                            if '_' not in word_two_empty:
                                round_two = True
                            #
                            alpha = True

print('With round two complete, let\'s see our totals!')
print(f'{player_one} has ${players_tb[0]}')
print(f'{player_two} has ${players_tb[1]}')
print(f'{player_three} has ${players_tb[2]}')

# Finding player with most money:

maximum = max(players_tb)
richest_index = players_tb.index(maximum)
richest_player = players[richest_index]
richest_player_tb = players_tb[richest_index]

# Third Round: (I had an issue pre filling the word with r,s,t,l,n, and e. I could have done this with a lot of code, but I didn't have a nice/quick way of doing this)

print(f'\nIt looks like {richest_player} will be moving on to the final round for a big bonus!\nYou will now have three consonant guesses and one vowel guess on the final word')

given = ['r', 's', 't', 'l', 'n', 'e']
int_three = randint(0,len(words)-1)
word_three = words[int_three]
word_three_empty = '_' * len(word_three)
#
word_list_three = list(word_three_empty)
indices = [i for i, letter in enumerate(word_three) if letter in given]
for index in indices:
    word_list_three[index] in given
word_three_empty = ''.join(word_list_three)
#
print('\nLet\'s get our Final word:')
guessed_letters = []

last_round = False
while not last_round:
    first = False
    while not first:
        print(f'{word_three_empty}')
        consonant_one = input('\nWhat is your first consonant guess? ')
        if consonant_one.isalpha() == False:
            print('\nPlease enter a consonant')
        elif consonant_one in vowels:
            print('\nPlease enter a consonant')
        elif consonant_one not in word_three:
            print(f'\n{consonant_one} is not in the word')
            guessed_letters.append(consonant_one)
            first = True
        else:
            print(f'\n{consonant_one} is in the word')
            guessed_letters.append(consonant_one)
            #
            word_list_three = list(word_three_empty)
            indices = [i for i, letter in enumerate(word_three) if letter == consonant_one]
            for index in indices:
                word_list_three[index] = consonant_one
            word_three_empty = ''.join(word_list_three)
            #
            first = True
    second = False
    while not second:
        print(f'{word_three_empty}')
        consonant_two = input('\nWhat is your second consonant guess? ')
        if consonant_two.isalpha() == False:
            print('\nPlease enter a consonant')
        elif consonant_two in vowels:
            print('\nPlease enter a consonant')
        elif consonant_two in guessed_letters:
            print('Guess a new letter')
        elif consonant_two not in word_three:
            print(f'\n{consonant_two} is not in the word')
            guessed_letters.append(consonant_two)
            second = True
        else:
            print(f'\n{consonant_two} is in the word')
            guessed_letters.append(consonant_two)
            #
            word_list_three = list(word_three_empty)
            indices = [i for i, letter in enumerate(word_three) if letter == consonant_two]
            for index in indices:
                word_list_three[index] = consonant_two
            word_three_empty = ''.join(word_list_three)
            #
            second = True
    third = False
    while not third:
        print(f'{word_three_empty}')
        consonant_three = input('\nWhat is your third consonant guess? ')
        if consonant_three.isalpha() == False:
            print('\nPlease enter a consonant')
        elif consonant_three in vowels:
            print('\nPlease enter a consonant')
        elif consonant_three not in word_three:
            print(f'\n{consonant_three} is not in the word')
            guessed_letters.append(consonant_three)
            third = True
        else:
            print(f'\n{consonant_three} is in the word')
            guessed_letters.append(consonant_three)
            #
            word_list_three = list(word_three_empty)
            indices = [i for i, letter in enumerate(word_three) if letter == consonant_three]
            for index in indices:
                word_list_three[index] = consonant_three
            word_three_empty = ''.join(word_list_three)
            #
            third = True
    last = False
    while not last:
        print(f'{word_three_empty}')
        vowel_one = input('\nWhat is your guess for the vowel ')
        if vowel_one.isalpha() == False:
            print('\nPlease guess a vowel')
        elif vowel_one not in vowels:
            print('\nPlease guess a vowel')
        elif vowel_one not in word_three:
            print(f'\n{vowel_one} is not in the word')
            last = True
        else:
            print(f'\n{vowel_one} is in the word')
            #
            word_list_three = list(word_three_empty)
            indices = [i for i, letter in enumerate(word_three) if letter == vowel_one]
            for index in indices:
                word_list_three[index] = vowel_one
            word_three_empty = ''.join(word_list_three)
            #
            last = True
    print(f'{word_three_empty}')
    print('\nYou have five seconds to guess the word')
    timeout = 5
    t = Timer(timeout, print, ['Sorry, times up! Goodbye and better luck next time.'])
    t.start()
    final_guess = input('What is the word? ')
    t.cancel()
    if final_guess == word_three:
        prize = 10000
        total_prize = richest_player_tb + prize
        print(f'\nCongrats! You correctly guessed the word and earned an extra ${prize}. Your total prize is ${total_prize}')
        last_round = True
    elif final_guess != word_three:
        print(f'\nI\'m sorry but that is incorrect. Your total is ${richest_player_tb}')
        last_round = True
    else:
        last_round = True

print('\nGoodbye!\n')