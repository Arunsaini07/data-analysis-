import matplotlib.pyplot as plt

import numpy as np


data = np.random.randn(1000)
plt.hist(data, bins=30, color='lightblue', edgecolor='black', linewidth=1)

# plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'), medianprops=dict(color='red'))
plt.title("Histogram")
plt.show()