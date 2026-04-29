# Check if a number is divisible by 5 using shorthand.

num = int(input("Enter a number: "))

result = "Divisible by 5" if num % 5 == 0 else "Not divisible by 5"
print(f"The number {num} is", result)