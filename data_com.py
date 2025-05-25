import matplotlib.pyplot as plt
import numpy as np

# Digital data
data = [1, 0, 1, 1, 0, 0, 0, 1]

# Time parameters
bit_duration = 1  # Duration of each bit
t = np.linspace(0, len(data) * bit_duration, len(data) * 100)  # Time array for smooth plotting
signal_nrz_l = []
signal_nrz_i = []
signal_manchester = []
signal_ami = []

# NRZ-L: 1 = +1V, 0 = -1V
for bit in data:
    if bit == 1:
        signal_nrz_l.extend([1] * 100)  # +1V for 1
    else:
        signal_nrz_l.extend([-1] * 100)  # -1V for 0

# NRZ-I: Change voltage for 1, no change for 0, start at -1V
current_level = -1
for bit in data:
    if bit == 1:
        current_level = -current_level  # Toggle voltage
    signal_nrz_i.extend([current_level] * 100)

# Manchester: 1 = +1 to -1, 0 = -1 to +1 (mid-bit transition)
for bit in data:
    if bit == 1:
        signal_manchester.extend([1] * 50 + [-1] * 50)  # +1 to -1
    else:
        signal_manchester.extend([-1] * 50 + [1] * 50)  # -1 to +1

# AMI: 0 = 0V, 1 = alternate +1/-1, start with +1 (after last 1 at -1)
last_one = -1  # Assume last 1 was -1V (per slide convention)
for bit in data:
    if bit == 0:
        signal_ami.extend([0] * 100)  # 0V for 0
    else:
        last_one = -last_one  # Alternate voltage for 1
        signal_ami.extend([last_one] * 100)

# Plotting
plt.figure(figsize=(10, 8))

# NRZ-L Plot
plt.subplot(4, 1, 1)
plt.plot(t, signal_nrz_l, drawstyle='steps-post')
plt.title('NRZ-L (1: +1V, 0: -1V)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, len(data) + 1, 1), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
plt.ylabel('Voltage')

# NRZ-I Plot
plt.subplot(4, 1, 2)
plt.plot(t, signal_nrz_i, drawstyle='steps-post')
plt.title('NRZ-I (1: Toggle, 0: No Change, Start -1V)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, len(data) + 1, 1), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
plt.ylabel('Voltage')

# Manchester Plot
plt.subplot(4, 1, 3)
plt.plot(t, signal_manchester, drawstyle='steps-post')
plt.title('Manchester (1: +1 to -1, 0: -1 to +1)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, len(data) + 1, 1), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
plt.ylabel('Voltage')

# AMI Plot
plt.subplot(4, 1, 4)
plt.plot(t, signal_ami, drawstyle='steps-post')
plt.title('AMI (0: 0V, 1: Alternate +1/-1, Start +1)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, len(data) + 1, 1), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
plt.ylabel('Voltage')
plt.xlabel('Bit Position (10110001)')

plt.tight_layout()
plt.show()