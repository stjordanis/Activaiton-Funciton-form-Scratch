import math
from matplotlib import pylab
import pylab as plt

xaxis = plt.linspace(-5,5,1000)
yaxis = []

for i in xaxis:
	if i<0:
		f=0
	else:
		f=1
	yaxis.append(f)
	
plt.title("Behaviour of Binary function")
plt.plot(xaxis,yaxis, linewidth=3)
plt.grid()
plt.show()