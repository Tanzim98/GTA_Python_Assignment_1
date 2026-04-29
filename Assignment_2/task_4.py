# Python Program to Find the Length of a List without using len()

def find_length(my_list):
    count = 0

    for item in my_list:
        count += 1

    return count

list = input("Enter list elements separated by space: ").split()

print("Length of list =", find_length(list))
