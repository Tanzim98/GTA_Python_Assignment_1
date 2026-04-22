# Find the largest of two numbers using if-else.

number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))

if number1 > number2:
    print(f"{number1} is largest number between {number2} and {number1}.")
elif number1 ==number2:
    (print(f"Both numbers are equal"))
else:
    print(f"{number2} is largest number between {number2} and {number1}")