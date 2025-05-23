import matplotlib.pyplot as plt                 

flower_type =['Rose','Lily','Dandelion','Marigold','Lotus','Tulip']
quantities = [6,5,3,4,2,1]
sort_accending = sorted(quantities)
top_three = [0,0,0]
top_three_flowers = ['', '', '']
for i in range(3):
        top_three[i] = sort_accending[5 - i]

for i in range(3):
    if(top_three[i]==6):
        top_three_flowers[i] = 'Rose'
    if(top_three[i]==5):
        top_three_flowers[i] = 'Lily'
    if(top_three[i]==4):
        top_three_flowers[i] = 'Marigold'
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.bar(flower_type,quantities,color='g')
plt.xlabel('Flowers')
plt.ylabel('Quantities')
plt.title('Flower Type vs Total Quantity')
plt.subplot(1,2,2)
plt.bar(top_three_flowers,top_three,color='r')
plt.xlabel('Top Three Flowers')
plt.ylabel('Quantities')
plt.tight_layout()
plt.show()