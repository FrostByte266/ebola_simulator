from support import *
import matplotlib.pyplot as plt

data = loadData('conditions.json')
if data is None:
    exit(1)
#print(data)
for (key, value) in data.items():
    print("{}: {}".format(key, value))
'''
x,y = data
plt.plot(x,y)
plt.title("Projected ebola deaths")
plt.xlabel("Day")
plt.ylabel("Number of deaths")
plt.show()
'''