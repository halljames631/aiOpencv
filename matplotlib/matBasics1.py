import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(-4,4,.1)
y = x*x
y2 =x*x+2

plt.grid(True)
plt.xlabel('my x values')
plt.ylabel('my y values')
plt.title('my first graph')
# plt.axis([0,5,0,11])
plt.plot(x,y,'g-*',linewidth=2,markersize=7,label='green line')
plt.plot(x,y2,'r:o', linewidth=2,markersize=7, label='red line')
plt.legend(loc='upper center')
plt.show()