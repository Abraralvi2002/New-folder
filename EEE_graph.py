import matplotlib.pyplot as plt

#Data
Vs = [5.4, 6.2, 7.0, 8.2, 9.2, 10.2, 11.2, 12.3, 13.1, 15.3, 18.2, 19.3, 20.6, 21.8, 22.3]
Vz = [4.4, 5.0, 5.8, 6.8, 7.6, 8.3, 9.3, 9.9, 9.96, 9.97, 10.0, 10.0, 10.0, 10.0, 10.0]
Iz = [0.82, 0.92, 1.00, 1.26, 1.47, 1.56, 1.73, 1.86, 2.1, 2.2, 2.4, 3.1, 3.6, 3.8, 4.1]

#Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

#Plot Iz vs Vs
axs[0].plot(Vs, Iz, marker='o', color='blue')
axs[0].set_title('Zener Current (Iz) vs Supply Voltage (Vs)')
axs[0].set_xlabel('Supply Voltage Vs (V)')
axs[0].set_ylabel('Zener Current Iz (mA)')
axs[0].grid(True)

# Plot Iz vs Vz
axs[1].plot(Vz, Iz, marker='o', color='green')
axs[1].set_title('Zener Current (Iz) vs Zener Voltage (Vz)')
axs[1].set_xlabel('Zener Voltage Vz (V)')
axs[1].set_ylabel('Zener Current Iz (mA)')
axs[1].grid(True)

plt.tight_layout()
plt.savefig("zener_diode_graphs.png")  # Save as image
plt.show()