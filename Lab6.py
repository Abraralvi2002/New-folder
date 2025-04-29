import matplotlib.pyplot as plt   
import numpy as np

House_length = [120,135,150,165,175]
House_price1 = [22000,33000,45000,55000,65000]
House_price2 = [12000,10000,55000,70000,40000]
'''House_price3 = [None] * 5

for i in range(5):
    House_price3[i] = House_price1[i] -  House_price2[i]'''
H1 = np.array(House_price1)
H2 = np.array(House_price2)
h = H1 - H2

plt.plot(House_length,House_price1,label ='Price 1',marker = 'd')
plt.plot(House_length,House_price2,label='Price 2',marker = 's')
plt.plot(House_length,h,label='Difference',marker = '<')

plt.title('House Price Prediction')
plt.xlabel('House Length')
plt.ylabel('House Price')
plt.legend()
plt.show()


