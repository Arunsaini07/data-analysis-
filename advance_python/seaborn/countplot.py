import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())
sns.countplot(x='day', data=df, palette='pastel')
plt.show()