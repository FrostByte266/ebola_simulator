from support import *
import matplotlib.pyplot as plt

data = loadData('previous-case-counts.csv')
#print(data)
x,y = data
plt.plot(x,y)
plt.title("Projected earthquake deaths in SF")
plt.xlabel("Year")
plt.ylabel("Number of deaths")
plt.show()