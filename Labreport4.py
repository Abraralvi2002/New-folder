import pandas as pd         

data = pd.read_excel("Assets/Lab_report_excel1.xlsx")

end = data.shape

for i in range(end[0]):
    data['A'][i] *= 2

for i in range(end[0]):
    data['B'][i] *= 2

for i in range(end[0]):
    sum = 0
    sum = data['A'][i] + data['B'][i]
    print(sum)