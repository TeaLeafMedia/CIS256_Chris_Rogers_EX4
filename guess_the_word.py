# Chris Rogers
# CIS256 Spring 2026
# Exercise Assignment 4

# import the random module for word selection
import random

def get_word(word, letters):
    display = ""
    for letter in word:
        if letter in letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Main game loop
def play_game():
    # Predefined list of words
    words = ["cheese", "basil", "tomato", "pasta"]
    
    # Select a random word
    secret = random.choice(words)
    
    guessed = []
    attempts = 6

    print("Wanna play Hangmam?")

    while attempts > 0:
        # Show current progress
        current_view = get_word(secret, guessed)
        print(f"\nWord: {current_view}")
        
        # Check if the whole word is revealed
        if "_" not in current_view:
            print("Great job! That's the word!")
            return

        # Get user input
        guess = input("What is your guess: ").lower()

        # Check if guess is correct or incorrect
        if guess in secret:
            print(f"'{guess}' is in the word, you're safe....for now.")
            guessed.append(guess)
        else:
            attempts -= 1
            print(f"'{guess}' is not there...the hangman draws closer. Attempts left: {attempts}")

    print(f"\nThe hangman has come for you. The word was: {secret}")

# call main to run the game 
if __name__ == "__main__":
    play_game()