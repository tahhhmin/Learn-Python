while True:
    unit = input("Is it Celcius [c] or Farenheit [f]: ").lower()
    if unit == 'c' or unit == 'f':
        break
    else:
        print("Enter a valid metric")

while True:
    try:
        temp = float(input("Enter your temp: "))
        break
    except ValueError:
        print("Enter a number")

if unit == 'c':
    converted = (temp * (180 / 100)) + 32
    display_unit = 'F'
else:
    converted = (temp - 32) * 100 / 180
    display_unit = 'C'

print(f"{round(converted, 2)} {display_unit}")