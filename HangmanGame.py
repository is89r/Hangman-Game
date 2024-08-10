import random

print("Welcome to Hangman Gaming!")

words = ["apple", "hacker", "bounty", "random"]
empty = []
secret_word = random.choice(words)
print("You get 5 Guesses")

for ltr in secret_word:
    empty += "_"
print(empty)

num = 0
game_over = False
while not game_over:
    guess = input("Guess a Letter !").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            empty[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"You have {guesses_left} guesses left")
        if num >= 5:
            print("You Loser!")
            game_over = True
    print(empty)
    if "_" not in empty:
        print("You Win!")
        game_over = True
