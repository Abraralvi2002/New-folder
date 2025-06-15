import matplotlib.pyplot as plt     
             
Flower = ['Rose', 'Lotus', 'Lily', 'Sun_Flower','Dandelion','Meri Gold']

rose_type =[10,50,30]
lotus_type =[10,76,45]
lily_type =[25,54,29]
sun_type = [12,32,67]
dandelion = [11,23,19]
m_type = [22,34,12]

plt.title('Flower Chart')
plt.bar('Rose',rose_type)
plt.bar('lotus',lotus_type)
plt.bar(Flower,lily_type)
plt.bar(Flower,sun_type)
plt.bar(Flower,dandelion)
plt.bar(Flower,m_type)

plt.show()