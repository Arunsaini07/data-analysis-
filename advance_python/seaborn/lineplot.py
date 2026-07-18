import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')


sns.lineplot(x='size', y='tip', data=df )
plt.show()