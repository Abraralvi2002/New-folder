import matplotlib.pyplot as p 
flower = ['Merigold','Lily','Tulip','Dandelion','Poppy']
flowernumber = [35,5,15,20,10]
fruit = ['Guava','Grape','Berry','Date','Peach']
fruitnumber = [10,5,4,20,6]
bird = ['Ostrich','Parrot','Vulture','Flamingo','Eagle']
birdnumber = [16,30,9,20,5]
vegetable = ['Bean','Bringle','Carrot','Radish','Ladies Finger']
vegnumb = [10,30,20,15,35]
fig = p.figure(figsize=(10,5))
fig.canvas.manager.set_window_title('Made By Md. Abrar Siddiqui CSE 63(D)')
p.subplot(2,2,1)
p.bar(flower,flowernumber,color='m')
p.xlabel('Flowers Name')
p.ylabel('Number of Flowers in Pieces')
p.title('Flowers vs Amount of Flowers')
p.subplot(2,2,2)
p.bar(fruit,fruitnumber,color='b')
p.xlabel('Fruit Name')
p.ylabel('Quantity of Fruits in Kilograms')
p.title('Fruits vs Amount of Fruits')
p.subplot(2,2,3)
p.bar(bird,birdnumber,color='g')
p.xlabel('Bird Name')
p.ylabel('Number of Birds in Sanctuary')
p.title('Birds vs Amount of Birds')
p.subplot(2,2,4)
p.bar(vegetable,vegnumb,color='c')
p.xlabel('Vegetables Name')
p.ylabel('Vegetable sold in Bags of 40 kg')
p.title('Vegetables vs Amount of Vegetables sold')
p.suptitle('Situation Based Bar Graph of: Flowers, Fruits, Birds, and Vegetables', fontsize=10)
p.tight_layout()
p.show()