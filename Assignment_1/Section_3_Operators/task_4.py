# Given a number, check if it is divisible by both 3 and 5.

number = int(input("Enter a number: "))
result = "is divisible" if number % 3==0 and number % 5==0 else "is not divisible"
print(f"Provided number {number}", result, "by both 3 and 5")