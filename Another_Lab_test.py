import numpy as np 
import matplotlib.pyplot as plt                                     
n = 5
len1 = [1,2,3,4,5]
ar1 = np.array([10,20,30,40,50])
ar2 = np.array([2,4,65,2,3,4,8,22,12,32])
ar3 = np.array([32,45,7,11,85,94,55,57,2,43,7,21,45,23,67])
ar4 = np.array(n)
for i in range(n):
    ar4 = ar1 + ar2[0:n]
print(ar4)

plt.plot(len1,ar1,label='Array 1',marker='>')
plt.plot(len1,ar4,label='Resulted Array',marker='s')
plt.title('Original Array & Resulted Array')
plt.xlabel('Length of Array')
plt.ylabel('Values of Array')
plt.legend()
plt.tight_layout()
plt.show()