import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('tips')
print(df.corr(numeric_only=True))
sns.heatmap(df.corr(numeric_only=True), annot=True )
plt.show()