import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 8)
sales = np.array([2.5, 3.0, 4.2, 5.1, 6.0, 7.5, 8.0])
plt.figure(figsize=(10, 5))

 # fasttype style use kiya hai
plt.style.use('fast')


# graph line np.doted hogi
plt.plot(days, sales,color ='b',label='sales in crores',linestyle='dotted',marker='o')
plt.title("Weekly Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.savefig("weekly_sales.png")  # Save the figure as a PNG file
plt.show()