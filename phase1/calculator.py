operations = ['+', '-',  "*", "/"]
calculation = 0
turn = 0

while True:
    operation = input("Please enter your operation: ").lower()
    if not operation in operations:
        print("Please select a valid operation")
    else:
        if turn == 0:
            while True:
                try: 
                    num1 = int(input("Enter your first number: "))
                    break
                except ValueError:
                    print("Please enter a valid integer")
        while True:
            try:
                num2 = int(input("Enter your second number: "))
                break
            except ValueError:
                print("Please enter a valid integer")

        if operation == '+' and turn == 0:
            result = num1 + num2
        elif operation == '+' and turn != 0:
            result = calculation + num2

        elif operation == '-' and turn == 0:
            result = num1 - num2
        elif operation == '-' and turn != 0:
            result = calculation - num2

        elif operation == "*" and turn == 0:
            result = num1 * num2
        elif operation == '*' and turn != 0:
            result = calculation - num2

        elif operation == '/' and turn == 0:
            result = num1/num2
        else:
            result = calculation/num2

        calculation += result

        print(round(result, 2))

        calc_again = input("Want to use the previous value? [y]/[n]: ").lower()
        if calc_again == 'y':
            turn += 1
        else:
            break