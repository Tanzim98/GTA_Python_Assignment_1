# Write a program using logical operators to check if a number is between 10 and 50.

number = int(input("Enter any number: "))
result = "not between" if number>50 else "not between" if number<10 else "between"
print(f"provided number {number} is", result, "10 and 50")
