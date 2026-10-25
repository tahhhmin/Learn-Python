import random

computer_guess = random.randint(0, 100)
tries = 0

while True:
    while True:
        try: 
            user_guess = int(input("Enter your guess [0-100]: "))
            if user_guess < 0 or user_guess > 100:
                print("Please enter a number within range [0-100]")
                continue
            else:
                break
        except ValueError:
            print("Please enter an integer")

    tries += 1

    if user_guess > computer_guess:
        print("Guess lower!")
    elif user_guess < computer_guess:
        print("Guess Higher")
    else:
        print(f"You guesse right. You won! Tries: {tries}")
        break