# Check whether a number is positive, negative, or zero.

number = int(input("Enter a number: "))
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
print(f"Provided number {number} is", result)