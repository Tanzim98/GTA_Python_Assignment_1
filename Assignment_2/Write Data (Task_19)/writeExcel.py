import pandas as pd

# Employee dataset
data = {
    'Employee Name': [
        'Arafat Rahman',
        'Nusrat Jahan',
        'Tanvir Hasan',
        'Sadia Islam',
        'Mehedi Hasan',
        'Farzana Akter',
        'Imran Hossain',
        'Tanjim Emon',
        'Shakib Ahmed',
        'Jannatul Ferdous'
    ],

    'Blood Group': [
        'A+',
        'B+',
        'O+',
        'AB+',
        'A-',
        'B-',
        'O-',
        'AB-',
        'A+',
        'O+'
    ]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Print dataset
print("Employee Data:")
print(df)
df.to_excel('employeeData.xlsx', index=False)