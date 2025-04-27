import numpy as np 
max = 0
a = np.array([10,3,5,7,20,15])
for i in range(6):
    if(a[i] > max):
        max = a[i]
print(max)