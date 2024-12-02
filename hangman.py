import random

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main_game():
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]
    dead_man = [
        """
           -----
           |   |
           X   |
          /|\  |
          / \  |
               |
        =========
        """
    ]
    words = ["cat","harry","meow"]
    word = choose_word(words)
    max_wrong_guesses = len(hangman_stages) - 1
    wrong_guesses = 0
    guessed_letters = set()

    print("Welcome to Hangman!")
    
    while wrong_guesses < max_wrong_guesses:
        print(hangman_stages[wrong_guesses])
        print("\n" + display_word(word, guessed_letters))
        #print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1
    
    if wrong_guesses == max_wrong_guesses:
        print(f"You lost! The word was: {word}. Also, you killed a man. Monster.")

main_game()
