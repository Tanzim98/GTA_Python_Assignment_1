# Take a student's marks and print grade

mark = int(input("Enter Students Mark: "))
if mark >= 90:
    print("The student gets A")
elif mark >= 75 and mark < 90:
    print("The student gets B")
elif mark >= 50 and mark < 75:
    print("The student gets C")
else:
    print("The student failed")