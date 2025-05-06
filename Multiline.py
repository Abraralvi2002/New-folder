import matplotlib.pyplot as p                   
import numpy as n                     
import math

a1 = n.array([3,4,6,2,10,5,8,12,22,7])

a2 = a1*2
a3 = a1*3

total_index = [0,1,2,3,4,5,6,7,8,9]

p.plot(total_index,a1,label='Array 1',marker='s')
p.plot(total_index,a2,label='Array 2',marker='o')
p.plot(total_index,a3,label='Array 3',marker='>')

p.title('Array Index vs Value')
p.xlabel('Array Index Number')
p.ylabel('Array Value Output')
p.legend()
p.show()
