import random
import re


def check_input(symbol, available_letters):
    if len(symbol) != 1:
        print('Please, input a single letter.')
    elif not re.fullmatch(r'[a-z]', symbol):
        print('Please, enter a lowercase letter from the English alphabet.')
    elif symbol in available_letters:
        print("You've already guessed this letter.")
    else:
        return True
    return False


def game():
    guess_words = ['python', 'java', 'swift', 'javascript']
    random_word = guess_words[random.randrange(4)]
    right_letters = set(random_word)
    available_letters = set()
    hidden_word = "-" * (len(random_word))
    attempts = 8

    while attempts > 0:
        letter = input(f'\n{hidden_word}\nInput a letter:')
        if not check_input(letter, available_letters):
            continue
        available_letters.add(letter)

        if letter in right_letters:
            hidden_word = ''.join([j if j in available_letters else '-' for j in random_word])
            if '-' not in hidden_word:
                print(f'\nYou guessed the word {random_word}!')
                print('You survived!')
                return True
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1

    print('You lost!')
    return False


print('H A N G M A N')
win_res = 0
lost_res = 0
menu = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
menu_choose = input(menu)

while menu_choose != 'exit':
    if menu_choose == 'play':
        is_win = game()
        if is_win:
            win_res += 1
        else:
            lost_res += 1
    elif menu_choose == 'results':
        print(f'You won: {win_res} times.')
        print(f'You lost: {lost_res} times.')
    menu_choose = input(menu)
