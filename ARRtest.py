#Code has issue.....
import numpy as np

n = int(input("Enter the size of array: \n"))
cz = 0 
co = 0
cw = 0
arr = np.zeros(n, dtype=int)  

for i in range(n):  
    arr[i] = int(input(f"Enter elements (The entries must be in zero and one) {i+1}: "))  
    if(arr[i] == 0):
        cz+= 1
    elif(arr[i] == 1):
        co+= 1
    else:
        cw+= 1 
print(f"The number of zeros inputed: {cz},\nThe number of one inputed: {co},\nThe number of wrong input: {cw}")
if(cz > co):
    if(cz > cw):
        print(f"Maxium input is zero, Total {cz} times")
elif(co > cw):
    print(f"Maximum inputs are one, Total {co} times")
    
else:
    print(f"Maximum inputs are wrong input, Total wrong inputed {cw} times")
    