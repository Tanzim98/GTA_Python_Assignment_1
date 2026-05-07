# Python Program to Remove Even Numbers from a List

def remove_even(numbers):
    result = []

    for num in numbers:
        if num % 2 != 0:
            result.append(num)

    return result

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", lst)
print("After removing even numbers:", remove_even(lst))