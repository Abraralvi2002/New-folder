import matplotlib.pyplot as mpl 

Flower = ['Rose', 'Lotus', 'Lily', 'Sun_Flower']
Amount_of_Flowers = [60,50,30,40]
Fruit = ['Apple', 'Mango', 'Orange', 'Banana']
Amount_of_Fruit = [40,70,60,20]
mpl.figure(figsize=(30,15))
mpl.subplot(2,1,1)
mpl.bar(Flower,Amount_of_Flowers,color= 'c')
mpl.xlabel('Flower')
mpl.ylabel('Amount of Flower')
mpl.title('Flower vs Amount of Flower')

mpl.subplot(2,1,2)
mpl.bar(Fruit,Amount_of_Fruit,color= 'g')
mpl.xlabel('Fruits')
mpl.ylabel('Amount of Fruit')
mpl.title('Fruit vs Amount of Fruit')
mpl.show()