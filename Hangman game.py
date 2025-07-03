import random

def play_hangman():
    words = ['apple', 'banana', 'grape', 'orange', 'mango', 'cherry', 'peach', 'melon', 'kiwi', 'papaya']
    word = random.choice(words)
    guessed_letters = []
    wrong_letters = []
    attempts = 6
    display = ['_'] * len(word)

    print("Welcome to Hangman!")
    print("Guess the word by entering one letter at a time.")
    print(f"The word has {len(word)} letters.")

    while attempts > 0 and '_' in display:
        print("\nWord: " + " ".join(display))
        print("Wrong guesses:", ", ".join(wrong_letters) if wrong_letters else "None")
        print("Lives left: " + ("♥ " * attempts))

        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
            wrong_letters.append(guess)

    if '_' not in display:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

def main():
    while True:
        play_hangman()
        again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if again != 'yes':
            print("Thanks for playing Hangman. Goodbye!")
            break

main()
