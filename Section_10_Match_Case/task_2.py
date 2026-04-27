# Input a number (1-7) and print the day of the week.

num = int(input("Enter a number (1-7): "))

match num:
    case 1:
        print("Day = Saturday")
    case 2:
        print("Day = Sunday")
    case 3:
        print("Day = Monday")
    case 4:
        print("Day = Tuesday")
    case 5:
        print("Day = Wednesday")
    case 6:
        print("Day = Thursday")
    case 7:
        print("Day = Friday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")