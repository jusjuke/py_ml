import matplotlib.pyplot as plt

# Sample data
x_data = [1, 2, 3, 4, 5]
y_data = [10, 12, 8, 15, 11]

# Create a simple line plot
plt.plot(x_data, y_data, 'ro-', linewidth=2, markersize=8, label='Data Points')

# Customize the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
plt.legend()

# Show the plot
plt.show()