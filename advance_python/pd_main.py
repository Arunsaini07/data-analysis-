import pandas as pd

df = pd.read_csv('data.csv' , skiprows=5, names=['Duration', 'Pulse', 'Maxpulse', 'Calories'])

print(df)

print(df[["Duration", "Pulse"]])
#   selelct all. columns where duration is greater than 5
# print(df[df['Duration'] > 50])

# select 
# import openpyxl

# workbook = openpyxl.load_workbook("students.xls")

# sheet = workbook.activep

# for row in sheet.iter_rows():
#     print(row[0].value, row[1].value, row[2].value)


df2 = pd.read_excel("random_data.xls")

print(df2)

print(pd.read_excel("random_data.xls", sheet_name="Sheet1"))



