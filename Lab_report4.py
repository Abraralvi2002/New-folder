import numpy as np    
import matplotlib.pyplot as plt                           

ar1 = np.array([10, 15, 20, 25, 30, 35, 40])
ar2 = np.array([5, 8, 12, 18, 22, 28, 35])

res_ar = ar1 - ar2

index = [0,1,2,3,4,5,6]

plt.figure(figsize=(10,6))

plt.plot(index,ar1,marker='o',label='Array 1')
plt.plot(index,ar2,marker='s',label='Array 2')
plt.plot(index,res_ar,marker='^',label='Subtracted Array')

plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Array Values and Their Element-wise Subtraction')
plt.tight_layout()
plt.legend()
plt.show()