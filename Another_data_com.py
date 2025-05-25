import matplotlib.pyplot as plt
import numpy as np

# Digital data
data = [1, 0, 1, 1, 0, 0, 0, 1]

# Time parameters
bit_duration = 1  # Duration of each bit
t = np.linspace(0, len(data) * bit_duration, len(data) * 100)  # Time array for smooth plotting
signal_nrz_i = []

# NRZ-I: Change voltage for 1, no change for 0, start at -1V
current_level = -1  # Initial voltage as per slide convention
inversion_points = []
non_inversion_points = []

for i, bit in enumerate(data):
    if bit == 1:
        current_level = -current_level  # Toggle voltage for 1
        inversion_points.append(i)  # Mark inversion point (start of bit)
    else:
        non_inversion_points.append(i)  # Mark non-inversion point (start of bit)
    signal_nrz_i.extend([current_level] * 100)

# Plotting
plt.figure(figsize=(10, 3))
plt.plot(t, signal_nrz_i, drawstyle='steps-post', label='NRZ-I')

# Annotate inversion points (1s)
for point in inversion_points:
    plt.annotate('Invert', xy=(point, signal_nrz_i[point * 100]), xytext=(point, signal_nrz_i[point * 100] + 0.5),
                 arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red')

# Annotate non-inversion points (0s)
for point in non_inversion_points:
    plt.annotate('No Invert', xy=(point, signal_nrz_i[point * 100]), xytext=(point, signal_nrz_i[point * 100] - 0.5),
                 arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')

# Customize plot
plt.title('NRZ-I for 10110001 (1: Toggle, 0: No Change, Start -1V)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, len(data) + 1, 1), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
plt.ylabel('Voltage')
plt.xlabel('Bit Position (10110001)')
plt.legend()

plt.tight_layout()
plt.show()