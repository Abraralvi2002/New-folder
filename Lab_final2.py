import matplotlib.pyplot as plt                    
import numpy as np                   

n = 3
len1 = np.array([1,2,3])
len2 = np.array([1,2,3,4,5,6])
len3 = np.array([1,2,3,4,5,6,7,8,9])
ar1 = np.array([10,20,30])
ar2 = np.array([40,50,60,70,80,90])
ar3 = np.array([100,110,120,130,140,150,160,170,180])

arsum = ar1 + ar2[0:n]

plt.title('Array vs Sum of Array')
plt.plot(ar1,len1,label='Array 1',marker='o')
plt.plot(ar2,len2,label='Array 2',marker='s')
plt.plot(ar3,len3,label='Array 3',marker='>')
plt.plot(arsum,len1,label='Sum of Array',marker='<')
plt.xlabel('Arrays')
plt.ylabel('Number of elements')
plt.tight_layout()
plt.legend()
plt.show()