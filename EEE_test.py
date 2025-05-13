import matplotlib.pyplot as plt

# Data from the table
vbe_1v = [0.100, 0.200, 0.300, 0.400, 0.200, 0.599, 0.677, 0.711, 0.729, 0.739, 0.753, 0.763, 0.769, 0.775, 0.779]  # V_BE for V_CE = 1V
ib_1v = [0, 0, 0, 0, 0, 0, 0, 0.89, 1.71, 2.61, 4.47, 6.37, 8.31, 10.3, 12.2]  # I_B for V_CE = 1V (μA)

vbe_10v = [0.100, 0.200, 0.300, 0.400, 0.500, 0.599, 0.677, 0.711, 0.729, 0.739, 0.753, 0.763, 0.769, 0.775, 0.779]  # V_BE for V_CE = 10V
ib_10v = [0, 0, 0, 0, 0, 0, 0, 0.89, 1.71, 2.61, 4.47, 6.37, 8.31, 10.3, 12.2]  # I_B for V_CE = 10V (μA)

# Create the plot
plt.figure(figsize=(6, 4))
plt.plot(vbe_1v, ib_1v, marker='o', label='V_CE = 1 V', color='blue')
plt.plot(vbe_10v, ib_10v, marker='o', label='V_CE = 10 V', color='red', linestyle='--')

# Label the axes
plt.xlabel('V_BE (V)')
plt.ylabel('I_B (μA)')

# Title and legend
plt.title('Input Characteristics of NPN Transistor')
plt.legend()

# Add annotation for saturation region (approximate based on the image)
plt.annotate('Saturation region', xy=(0.75, 2), xytext=(0.65, 8),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Set axis limits to match the style of the image
plt.xlim(0, 0.8)
plt.ylim(0, 15)

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.show()