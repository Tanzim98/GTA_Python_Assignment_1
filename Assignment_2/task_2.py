# Python Program to Calculate Factorial of a Number (using function)

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

number = int(input("Enter a number: "))

print(f"Factorial of {number} =", factorial(number))