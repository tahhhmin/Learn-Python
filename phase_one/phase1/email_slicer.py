email = input("Enter your email: ").lower()

try: 
    index = email.index("@")
    address = email[:index]
    provider = email[(index +  1):]

    print(f"Your address: {address} and provider is {provider}")
except:
    print("Could not index")



