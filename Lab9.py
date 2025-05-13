import pandas as pd                        
df = pd.read_excel("C:/Users/abrar/OneDrive/Desktop/Lab9.xlsx")
print(df.to_string(index=False))
sumx = 0
sumy = 0
t = df.shape
for i in range (t[0]):
    sumx += df['x'][i]

for i in range (t[0]):
    sumy += df['y'][i]

print(sumx)
print(sumy)