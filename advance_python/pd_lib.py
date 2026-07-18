import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']*1,
    'Age': [25, 30, 35, 40, 45,None , 55,60, 65, 70]*1,
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']*1,
    'Married': ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no']*1
}
df = pd.DataFrame(data)
print(df[df['Married'] == 'yes'])
print(df[df['Age'] > 40])  
#abi hum age sum ko print krenge
print(df['Age'].sum())
print(df.dropna())  # Check for missing values
# print(df)
df["Age"] = df["Age"].fillna(0)
print(df)
print(df.dtypes)
# df["Name"] = df["Name"].str.lower().str.strip()
# print(df.head() )
df["Category"] = df["Name"].str.lower().str.strip()
print(df.head() )
