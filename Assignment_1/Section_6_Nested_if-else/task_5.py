# Determine ticket price:

age = int(input("Enter your age: "))

if age < 5:
    print("You will get free ticket")
elif age <= 18:
    print("You will get ticket in discount price")
else:
    print("You have to provide full ticket price")
