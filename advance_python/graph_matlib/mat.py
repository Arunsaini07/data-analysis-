import matplotlib.pyplot as plt

import numpy as np

x=[1,2,3,4,5]
y=[1,12,14,19,2]

plt.plot(x,y , color='brown', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.title("Matplotlib demo")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()