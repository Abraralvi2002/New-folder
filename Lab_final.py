import pandas as pd           

data = pd.read_excel("C:/Users/abrar/OneDrive/Desktop/Lab_final.xlsx")
t = data.shape

lowest_price = 999999999
model = ""

for i in range(t[0]):
    price = data['car_price'][i]
    model = data['car_model'][i]
    
    if price < lowest_price:
        lowest_price = price
        model = model
    
        
print("Car with the lowest price:")
print("Car Model:",model)
print("Price:", lowest_price)