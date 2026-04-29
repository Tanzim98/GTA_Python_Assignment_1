#Count how many vowels are in a given string.

string = input("Enter a string: ")

count = 0

for character in string:
    if character in "aeiouAEIOU":
        count = count + 1

print(f"the given string has", count, "vowels")
