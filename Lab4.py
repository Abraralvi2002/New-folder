import matplotlib.pyplot as plt 
category = ['mango','banana','apple']
quantity = [20,50,30]
plt.figure(figsize=(30,10))
plt.bar(category,quantity,color='c')
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.title('Category vs Quantity Graph')
plt.show()