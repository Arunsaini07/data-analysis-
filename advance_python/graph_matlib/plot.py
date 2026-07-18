import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)   

plt.figure(figsize=(8, 6))


plt.style.use('ggplot')  # Set the style to 'ggplot' for a different look
plt.plot(x, y, color='lightblue', linewidth=2)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
  # Set the style to 'dark_background' for a different look
plt.savefig("line_plot.pdf")  # Save the plot as a PNG file

plt.show()