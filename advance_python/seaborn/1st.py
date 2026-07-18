import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# print(df.head())

sns.scatterplot(x='total_bill', y='tip', data=df, hue='size', style='time', palette='deep', s=100)
plt.title('Scatter Plot of Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()


