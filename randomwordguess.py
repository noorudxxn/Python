import random
words = ["apple", "banana", "orange", "mango", "grapes", "python", "javascript", "django", "computer", "programming"]
word = random.choice(words)

guessed_characters = []
attempts = 6

display_word = ""

for character in word:
    if random.choice([True, False]):
        display_word += character
    else:
        display_word += "_"


for i in range(len(word)):
    if display_word[i] != "_":
        guessed_characters.append(word[i])

print("WELCOME TO THE WORD GUESSING GAME!")
print("Guess the word:", " ".join(display_word))

while attempts > 0:

    guess = input("Guess a character: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_characters:
        print("Character already guessed!")
        continue

    guessed_characters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1


    display_word = ""

    for character in word:
        if character in guessed_characters:
            display_word += character
        else:
            display_word += "_"

    print("Word:", " ".join(display_word))
    print("Remaining attempts:", attempts)


    if all(character in guessed_characters for character in word):
        print("Congratulations! You guessed the word:", word)
        break

else:
    print("Game over! The word was:", word)