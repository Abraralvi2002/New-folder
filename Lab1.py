import numpy as np
sum = 0
a = np.array([1,2,3,4,5])
for i in range(0,5,1):
    print(a[i])
    sum += a[i]
print(sum)
