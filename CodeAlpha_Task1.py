import random

def choose_word():
    words = ["yamaha", "hero", "ninja", "pulsar", "bmw", "tvs"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 5
    incorrect_attempts = 0
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_attempts += 1
            print("Incorrect guess. Attempts left:", max_attempts - incorrect_attempts)
        else:
            print("Correct guess!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break

    if "_" in current_display:
        print("Sorry, you've run out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
