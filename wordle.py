
#######################################################
# wordle
#########################################################

# This is the "main" portion of your game.
# Any code that uses stdin or stdout (i.e., input() and print())
# should go in this file.

import wordle_engine
import sys
import random

# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")
def is_valid_guess(guess, valid_word_list):
    # this is a function that verifies that a word is valid, by traversing through a text file of valid words to
    # see if that word is there. It takes the user's guess and the text file as parameters.
    if guess in valid_word_list:
        return True

def choose_hidden_word(word_list: set):
    # a function that randomly chooses the hidden word from the text file of wordles
    hidden_word = random.choice(tuple(word_list))
    return hidden_word


# Use the target word provided on the command line,
# or, choose a random word if no target word given.
if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    # TODO choose a random word from valid_words
    words = wordle_engine.load_words('shuffled_real_wordles.txt')
    target = choose_hidden_word(words)

# TODO Implement the rest of the game.
guess_number = 0
abc_dict = wordle_engine.create_letter_status()
guess_list = []
while guess_number <= 6:
    guess = input("Please enter a 5 letter word: ").strip().lower()
    if is_valid_guess(guess, valid_words) is True:
        colored_guess = wordle_engine.format_guess(target, guess)
        guess_list.append(colored_guess)
        for guess_colored in guess_list:
            print(guess_colored)
        if guess == target:
            print("You Won!!")
            break
        colored_abc = wordle_engine.update_letter_status(abc_dict, target, guess)
        print(wordle_engine.format_letters(colored_abc))
        guess_number += 1
        print("Guess number:", guess_number)
        if guess_number == 6:
            print("YOU LOST :( Better luck next time... The word was", target)
    elif len(guess) != 5:
        print("A guess needs to be five letters")
    else:
        print("That is not a valid word")
