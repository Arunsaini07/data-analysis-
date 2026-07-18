import matplotlib.pyplot as plt

import numpy as np

sizes = [215, 130, 245, 210]
labels = ['XXL', 'XL', 'L', 'M ']
plt.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%', explode=(0.1, 0, 0, 0), colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue'])
plt.title("Pie Chart")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.show()
