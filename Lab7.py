# f(x) = x^3 - x - 2 
import math
x = 2
e = 0.000001
flag = 0
while(1):
    f_x = x**3 - x - 2
    f2_x = 3*x**2 - 1
    x2 = x - (f_x / f2_x)
    x = x2
    if(abs((x2-x)/x2)<=e):
        print(x2)
        flag = 1
        break
    
if(flag==0):
    print("Incorrect initial guess.")   
        
    