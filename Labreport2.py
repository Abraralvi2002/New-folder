import matplotlib.pyplot as p                         

fruits = ["Apple","Banana","Orange","Grape","Mango"]
bd_price = [3.00,0.90,2.70,3.40,1.50]
usa_price = [4.50,1.20,2.50,4.40,3.00]
uk_price = [4.0,1.10,3.00,4.30,3.20]
fig = p.figure(figsize=(10,5))
fig.canvas.manager.set_window_title('Made By Md. Abrar Siddiqui-1294 CSE 63(D)')
p.plot(fruits,bd_price,label='Price in BD',color='green',marker='o')
p.plot(fruits,usa_price,label='Price in USA',color='red',marker='o')
p.plot(fruits,uk_price,label='Price in UK',color='blue',marker='o')

p.title('Price of Common Fruits in Different Countries for Per Kilograms in USD$')
p.xlabel('Name of The Fruits')
p.ylabel('Prices of Fruits')
p.legend()
p.show()