#######################################################
# wordle_engine
#########################################################


# Container for color control codes.
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def welcome_string():
    string = f"Welcome to {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r\
        {wordle_colors.YELLOW}d{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"
    return string.replace("  ", "")

def create_letter_status():
    """ Initialize and Return a new dictionary that maps each letter to
        wordle_colors.BLUE """
    wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"
    # creates a dictionary of all of the letters in blue
    alphabet_dict = {}
    for letter in wordle_alphabet:
        alphabet_dict[letter] = f"{wordle_colors.BLUE}"
    return alphabet_dict

def load_words(filename: str):
    """ Load the words from the specified file and place them
        in a set.
        Ignore any lines that begin with "#"
        """
    # opens up text files and loads words into a list of ind words
    words = set()
    with open(filename) as f:
        while True:
            line = f.read().splitlines()
            for word in line:
                if word[0] != "#":
                    words.add(word)
            return words

def format_guess(target, guess):
    """ Return a string that contains the user's guess formatted
        so that each letter is colored
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word,
                  but in a different location.
        * RED:    The letter does not appear in the target word
        Also, the string should end with wordle_colors.ENDC """
    guess_list = [" "] * len(guess)
    string = ""
    index = -1
    for letters in guess:
        index += 1
        if letters in target:
            # if the letter belongs in the green list
            if guess[index] == target[index]:
                guess_list[index] = f"{wordle_colors.GREEN}{letters}"
            # if the letter belongs in the yellow lsit
            else:
                guess_list[index] = f"{wordle_colors.YELLOW}{letters}"
        # if the letter belongs in the red list
        else:
            guess_list[index] = f"{wordle_colors.RED}{letters}"
    for keys in guess_list:
        string += keys
    string += wordle_colors.ENDC
    return string

def update_letter_status(letter_status: dict, target, guess):
    """ Update the letter status dictionary to show which letters
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""
    index = -1
    # The letters are placed in a list for their appropriate color
    for letter in guess:
        index += 1
        if letter in target:
            # if the letter belongs in the green list
            if guess[index] == target[index]:
                letter_status[letter] = f"{wordle_colors.GREEN}"
            # if the letter belongs in the yellow lsit
            else:
                if letter_status[letter] == f"{wordle_colors.GREEN}":
                    break
                letter_status[letter] = f"{wordle_colors.YELLOW}"
        # if the letter belongs in the red list
        else:
            letter_status[letter] = f"{wordle_colors.RED}"
    return letter_status

def format_letters(letter_status):
    """ Generate a string that lists all the letters of the alphabet
    colored according to the rules given in update_letter_status.
    the string should end with wordle_colors.ENDC """
    string = ""
    for finalabc in letter_status:
        string += letter_status[finalabc] + finalabc
    string += wordle_colors.ENDC
    return string
