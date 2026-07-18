import pandas as pd


df = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'customer_id': [101, 102, 103, 104],
    'order_amount': [250, 150, 300, 400],
    'order_date': [
        '2023-01-01',
        '2023-01-02',
        '2023-01-03',
        '2023-01-04'
    ],
    'customer_name': [
        'Alice',
        'Bob',
        'Charlie',
        'David'
    ],
    'customer_country': [
        'USA',
        'Canada',
        'UK',
        'Australia'
    ]
})


print(df)


df.to_csv(
    "data.csv",
    index=False
)