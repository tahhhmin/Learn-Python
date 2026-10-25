import random

moves = ["r", "p", "s"]

computer_score = 0
user_score = 0

while True:
    computer_move = random.choice(moves)

    while True:
        user_move = input("Please choose Rock [r], Paper [p], Scissor [s]: ").lower()
        if not user_move in moves:
            print("Enter a valid input")
            continue
        else:
            break

    if user_move == computer_move:
        print("You both picked the same")

    elif (
        (user_move == 'r' and computer_move == 's') or 
        (user_move == 'p' and computer_move == 'r') or 
        (user_move == 's' and computer_move == 'p')
    ):
        print("You won!")   
        user_score += 1
    elif (
        (user_move == 'r' and computer_move == 'p') or 
        (user_move == 'p' and computer_move == 's') or 
        (user_move == 's' and computer_move == 'r')
    ):
        print("Computer Won!")
        computer_score += 1

    print(f"Player: {user_score} | Computer: {computer_score}")

    if computer_score == 10 or user_score == 10:
        break