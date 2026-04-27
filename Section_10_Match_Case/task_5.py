ch = input("Enter a character: ")

if len(ch) != 1:
    type_char = "invalid"
elif ch in "aeiouAEIOU":
    type_char = "vowel"
elif ch.isdigit():
    type_char = "digit"
else:
    type_char = "consonant"

match type_char:
    case "vowel":
        print("Vowel")
    case "consonant":
        print("Consonant")
    case "digit":
        print("Digit")
    case _:
        print("Invalid input")