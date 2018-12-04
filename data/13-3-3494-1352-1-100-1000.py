
import matplotlib.pyplot as plt
file = open('13-3-3494-1352-1-100-1000.txt', 'r')
values = sorted([ int(i) for i in file.read().split() ])
plt.plot(values)
plt.show()