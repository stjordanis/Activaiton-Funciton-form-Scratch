import math
import matplotlib.pyplot as plt
xaxis = range(-10,11)
yaxis = []

for i in xaxis:
	if i<0:
		f=i*0.1
	else:
		f=i
	yaxis.append(f)
	

plt.title("Behaviour of leaky ReLU function")
plt.plot(xaxis,yaxis)
plt.grid()
plt.show()
