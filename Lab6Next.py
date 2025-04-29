import matplotlib.pyplot as plt                              
import numpy as np                  

x = np.linspace(-2*np.pi,2*np.pi)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y,marker='o')
plt.plot(x,y2,marker='s')
plt.title('Sinusoidal Wave')
plt.xlabel('Angle')
plt.ylabel('Amplitude')
plt.show()