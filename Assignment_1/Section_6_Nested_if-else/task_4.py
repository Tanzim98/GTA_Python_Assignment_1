# Check eligibility for a job:

age = int(input("Enter your age: "))
degree = input("Do you have a degree? (Yes/No): ")

if age >= 18 and degree == "Yes":
    print("You are eligible for the job")
else:
    print("You are not eligible for the job")