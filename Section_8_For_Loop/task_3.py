# Find the sum of numbers from 1 to N.

number = int(input("Enter a number: "))

total = 0
for i in range(1, number+1):
    total = total + i

print("Total Sum:", total)
