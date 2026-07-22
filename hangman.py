import random

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

words = ["python", "computer", "program", "SQL", "web devlopment" ,"java" ,"engineer" , "keyboard",
          "developer", "software", "network"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)

while wrong_guesses < max_wrong:

    print()
    for line in hangman_art[wrong_guesses]:
        print(line)

    # Display guessed word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win check
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("Try new letter, You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print(f"Remaining Attempts: {max_wrong - wrong_guesses}")

# Game Over
if wrong_guesses == max_wrong:
    print()
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("\n Game Over! You Loss")
    print("The correct word was:", word)

