def input_validation(type, text, min=False, max=False):
    user_input = ""
    
    while True:
        try:
            if type == 'int': 
                user_input = int(input(text))
            elif type == 'float':
                user_input = float(input(text))
            
            if min is not None and user_input < min:
                print(f"Please enter a value within range [{min}-{max}]")
                continue
            elif max is not None and user_input > max:
                print(f"Please enter a value within range [{min}-{max}]")
                continue

            return user_input

        except ValueError:
            print("Please enter a number")

output = input_validation('int', "Enter a valid integer with range: ", 0, 10)

print(output)