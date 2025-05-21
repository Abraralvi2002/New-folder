import pandas as pnd            
meow = pnd.read_excel("C:/Users/abrar/Downloads/Meow_Meow.xlsx")

sum_odd = 0
t = meow.shape
#print(t,end=" ")
for i in range(t[0],t-1):
    if(i%2 != 0 or i%3 != 0 or i%5 != 0 or i != 0):
        sum_odd += meow['A'][i]
        

print(sum_odd)