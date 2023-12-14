import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    
    # Choose a random word
    selected_word = choose_word()
    
    # Initialize variables
    guessed_letters = []
    attempts_left = 6
    
    while attempts_left > 0:
        # Display the current state of the word
        current_display = display_word(selected_word, guessed_letters)
        print(f"Word: {current_display}")
        
        # Prompt the user for a letter
        guess = input("Enter a letter: ").lower()
        
        # Check if the guessed letter is in the word
        if guess in selected_word:
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Incorrect! Attempts left: {attempts_left}")
        
        # Add the guessed letter to the list
        guessed_letters.append(guess)
        
        # Check if the word has been completely guessed
        if "_" not in display_word(selected_word, guessed_letters):
            print("Congratulations! You guessed the word.")
            break
    
    # If the player runs out of attempts
    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The word was: {selected_word}")

if __name__ == "__main__":
    hangman()
