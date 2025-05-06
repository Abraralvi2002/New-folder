import math

x1 = 50
x2 = 5
f_x1 = 3*x1**2 + 2*x2 + 2
f_x2 = 3*x1**2 + 2*x2 + 2

while(1):
    fx2 = 3*x2**2 + 2*x2 + 2
    if(x1==x2):
        print(x2)
        break
    else:
        if(f_x1-f_x2 == 0):
            print("The secant has no answer")
            break
        x2 =  (x1 - ((x1 - x2)/(f_x1 - f_x2))) * f_x1
        x1 = x2
        

