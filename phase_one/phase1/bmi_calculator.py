while True:
    try:     
        mass = float(input("Please enter your mass [kg]: "))
        if mass <= 0:
            print("Mass must be greater than zero.")
            continue
        break
    except ValueError:
        print("Please enter a number")

while True:
    try:     
        height = float(input("Please enter your height [meter]: "))
        if height <= 0:
            print("Height must be greater than zero.")
            continue
        break
    except ValueError:
        print("Please enter a number")

bmi = mass / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 19.5:
    print("You are under weight")
elif bmi < 24.5:
    print("Your weight is ideal")
elif bmi < 29.5:
    print("You are over weight")
else:
    print("You are obese")