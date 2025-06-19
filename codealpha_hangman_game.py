import random

words = ['apple', 'banana', 'grape', 'orange', 'mango']
word = random.choice(words)
guessed_letters = []
attempts = 6


display = ['_'] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word:")

while attempts > 0 and '_' in display:
    print("\n" + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        attempts -= 1
        guessed_letters.append(guess)
        print(f"Attempts left: {attempts}")

if '_' not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
