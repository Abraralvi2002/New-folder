import numpy as np
import matplotlib.pyplot as plt

n = 3
ar1 = np.array([1, 2, 3])
ar2 = np.array([4, 5, 6, 7, 8, 9])
ar3 = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18])
sum_ar = ar1 + ar2[0:n]

index1 = [0,1,2]
index2 = [0,1,2,3,4,5]
index3 = [0,1,2,3,4,5,6,7,8]
index_sum = [0,1,2]

plt.figure(figsize=(10,6))

plt.plot(index1, ar1, marker='o', label='Array 1')
plt.plot(index2, ar2, marker='s', label='Array 2')
plt.plot(index3, ar3, marker='^', label='Array 3')
plt.plot(index_sum, sum_ar, marker='>', label='Sum Array')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Original 3 Arrays & Sum of First Two Arrays')
plt.legend()

plt.tight_layout()
plt.show()