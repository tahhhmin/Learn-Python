import random

while True:
    user_input = input("Roll the dice [y]/[n]: ").lower()
    if user_input == 'y':
        roll = (random.randint(0, 6), random.randint(0,6))
        print(roll)
        continue 
    elif user_input == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")