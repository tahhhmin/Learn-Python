import random 

computer_guess = random.randint(0, 10)
guess_counter = 0

while guess_counter < 3:
    while True:
        try: 
            user_guess = int(input("Enter your guess [0-10]: "))
            if user_guess < 0 or user_guess > 10:
                print("Please enter within range")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    guess_counter += 1


    if user_guess > computer_guess:
        print("Guess lower")
    elif user_guess < computer_guess:
        print("Guess higher")
    else:
        print("You guessed correctly! You won")
        break 

    print(f"You have {3-guess_counter} guesses left")
    
    if user_guess != computer_guess and guess_counter == 3:
        print("You ran out of guesses. You lost")
        break