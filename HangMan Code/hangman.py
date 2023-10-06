# Coding Challenge 3, hangman.py
# Name:Loucas xiourouppa
# Student No:2007307

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt" #This decides what program to open

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]

""" this randomises the word you will get when running the program"""
def choose_random_word(all_words):
    return random.choice(all_words)


# end of helper code
# -----------------------------------

""" This function opens my txt file in read mode"""
def load_words():
    print("Loading word list from file:", WORDLIST_FILENAME)
    try:
        with open(WORDLIST_FILENAME, "r") as file:
            file_contents = file.read()
            words = file_contents.split()
            print(len(words), "words loaded")
            return words
    except OSError:
        print("Oops something broke!")
            
    
    


   
# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function


wordlist = load_words()

"""this function tells the user whether or not they got a letter correct"""
def is_word_guessed(word, letters_guessed):
    for letter in word:
        if not(letter in letters_guessed):
            return False
    return True



def get_guessed_word(word, letters_guessed):
    output = ""
    for letter in word:
        if letter in letters_guessed:
            output += letter
        else:
            output += "_ "
    return output 



def get_remaining_letters(letters_guessed):
    alphabet = ascii_lowercase
    for letter in alphabet:
        if letter in letters_guessed:
            alphabet = alphabet.replace(letter, "")
    return alphabet
        
        


def hangman(word):
    """this is my score which the user starts with 6 guesses"""
    score = 0
    guesses = 6
    letters_guessed = list()
    vowels = ["a", "e", "i", "o", "u"]
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))

    while True:
        finished = is_word_guessed(word, letters_guessed) or guesses < 1

        if finished:
            if is_word_guessed(word, letters_guessed):
                score = guesses * len(set(word))
                print(responces[2].format(score))
            elif guesses < 1:
                print(responses[3].format(word))
            break
               
        
        print("-------------")
        print(responses[4].format(guesses))
        print(responses[5].format(get_remaining_letters(letters_guessed)))
        guess = input("Please guess a letter: ").lower()
        if not(guess in letters_guessed):
            letters_guessed.append(guess)
            if guess in word:
                response = responses[6]
            else:
                response = responses[7]


                if guess in vowels:
                    guesses = guesses - 2
                else:
                    guesses = guesses - 1


        else:
            response = responses[8]
        print(response.format(get_guessed_word(word, letters_guessed)))


# ---------- Challenge Functions (Optional) ----------

def get_score(name):
    pass

def save_score(name, score):
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------
"""this is the main function that calls the functions"""
def main():
    wordlist = load_words()
    word = choose_random_word(wordlist)


    finished = False
    while not finished:
        hangman(word)
        again = input("Would you like to play again: (y/n) ").upper()
        while again not in ["Y", "N"]:
            again = input("Would you like to play again: (y/n) ").upper()
        if again == "N":
            finished = True




    

# Driver function for the program
if __name__ == "__main__":
    main()
