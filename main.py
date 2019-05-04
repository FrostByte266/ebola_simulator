from support import *
import matplotlib.pyplot as plt

data = loadData('data.csv')
#print(data)
x,y = data
plt.plot(x,y)
plt.title("Projected ebola deaths")
plt.xlabel("Day")
plt.ylabel("Number of deaths")
plt.show()