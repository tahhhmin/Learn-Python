import random
from words import words

word = []
revealed_word =  []

body = ['head', 'torso', 'spine']
tries = 0

for i in random.choice(words):
    word.append(i.capitalize())
for i  in range(len(word)):
    revealed_word.append("_" * 5)

while tries <= len(body):
    user_input = input("Enter your guess: ").capitalize()

    guessed_indexes = [idx for idx, val in enumerate(word) if val == user_input]

    for i in range(len(word)):
        if i in guessed_indexes:
            revealed_word[i] = word[i]
            
    print(" ".join(revealed_word))
    print(F"{random.choice(body)} Kete felsi")
    tries += 1

print("You did it!")