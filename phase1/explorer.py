import random
import time

hp = 100
gold = 0
level = 1

def input_validator(inputs):
    for i in range(len(inputs)):
        print(f"[{i}]: {inputs[i]}")
    while True:
        try:
            user_input = int(input(f"Please Enter Your Move [0-{len(inputs) - 1}]: ")) 
            if user_input < 0 or user_input > len(inputs) - 1:
                print(f"Please Stay Withing Range [0-{len(inputs) - 1}]")
                continue
            else:
                break
        except ValueError:
            print("Please Enter a Number")

    return user_input

def value_updater(change, changed_item):
    global hp, level, gold

    if changed_item == 0:
        gold = gold + change
    elif changed_item == 1:
        level = level + change
    else:
        hp = hp - change
        

def explore_room():
    rooms = ['Safe', 'Dangerous', 'Bountiful']
    picked_room = random.choice(rooms)
    print("Entering a new room")
    time.sleep(1)
    print(f"You Entered a New Room. Type: {picked_room}")

    if picked_room == 'Safe':
        safe_room_options = ['Loot', 'Collect XP']
        safe_room_move = input_validator(safe_room_options)

        if safe_room_move == 0:
            added_gold = random.randint(1, 50)
            print(f"You Earned {added_gold} Coins!")
            return added_gold, 0
        else:
            added_xp = random.randint(1, 10)
            added_xp = added_xp/10
            print(f"You Earned {added_xp} XP!")
            return added_xp, 1

    elif picked_room == 'Dangerous':
        dangerous_room_options = ['Fight', 'Try to run']
        dangerous_room_move = input_validator(dangerous_room_options)

        if dangerous_room_move == 0:
            fight_decider = random.randint(0, 5)

            if fight_decider == 0:
                print("You one shot the monster!")
                return 5, 1

            elif fight_decider == 1:
                print("You defeated the monster but got a few scratches")
                return 10, 3

            elif fight_decider == 2:
                print("You defeated the monster but got a little hurt")
                return 20, 3
            
            elif fight_decider == 3:
                print("You defeated the monster but got kinda hurt")
                return 30, 3
            
            elif fight_decider == 4:
                print("You defeated the monster but got badly hurt")
                return 40, 3         

            else:
                print("You couldn't defeat the monster and got fatally wounded")
                return 100, 3               

        else: 
            escape_decider = random.randint(0,1)
            if escape_decider == 0:
                print("You escaped safely")
                return 0, 0
            else:
                print("You escaped but with got hurt")
                return 50, 3

    else:
        bountiful_room_options = ['Loot', 'Collect XP']
        bountiful_room_move = input_validator(bountiful_room_options)

        if bountiful_room_move == 0:
            added_gold = random.randint(1, 200)
            print(f"You Earned {added_gold} Coins!")
            return added_gold, 0
        else:
            added_xp = random.randint(1, 100)
            added_xp = added_xp/10
            print(f"You Earned {added_xp} XP!")
            return added_xp, 1

def player_heal(): 
    global hp, gold
    heal_options = ['Full: Makes 100 [50]', 'Half: Plus 50 [25]', 'Small: Plus 25 [12]']
    
    heal_move = input_validator(heal_options)
    
    if gold >= 50 and heal_move == 0:
        gold = gold - 50
        hp = 100
    elif gold >= 25 and heal_move == 1:
        gold = gold - 25
        if hp > 50:
            hp = 100
        else:
            hp = hp + 50
    elif gold >= 12 and heal_move == 2:
        gold = gold - 12
        if hp > 75:
            hp = 100
        else:
            hp = hp + 25
    else:
        print("You dont have enough coins")

    

while hp > 0:
    print(f"Your Health: {hp}")
    print(f"Your Coins: {gold}")
    print(f"Your Level: {level}")
    initial_options = ['Explore Room', 'Heal', 'Exit']
    initial_move = input_validator(initial_options)

    if initial_move == 0:
        change, changed_item = explore_room()
        value_updater(change, changed_item)
    elif initial_move == 1:
        player_heal()
    else:
        print("Goodbye Player!")
        break

if hp < 1:
    print("You died. RIP")