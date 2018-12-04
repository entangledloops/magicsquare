
import matplotlib.pyplot as plt
file = open('5-3-3494-100-1-10-10000.txt', 'r')
values = sorted([ int(i) for i in file.read().split() ])
plt.plot(values)
plt.show()