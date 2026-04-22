# Check if a number is divisible by both 2 and 3.
number = int(input("Enter a number: "))

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by both 2 and 3")
else:
    print(number, "is not divisible by both 2 and 3")