import random

# Predefined word list
words = [
    "python", "coding", "laptop", "science", "engineer",
    "program", "hello", "computer", "study", "robot",
    "mathematics", "physics", "chemistry", "hangman",
    "developer", "keyboard", "internet", "software"
]

def hangman_game():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("\n🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.\n")
    print("The word has", len(word), "letters.")
    
    while attempts > 0:
        display_word = ""

        # Display current progress
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word.strip())
        print("Guessed Letters:", ", ".join(sorted(guessed_letters)))
        print("Remaining Attempts:", attempts)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

        guess = input("\nEnter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("✅ Good guess! Letter is in the word.")
        else:
            attempts -= 1
            print("❌ Wrong guess!")

    print("\n💀 Game Over! The word was:", word)


# Game loop for replay
while True:
    hangman_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("👋 Thanks for playing!")
        break
    
