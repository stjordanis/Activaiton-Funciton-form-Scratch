import math
import matplotlib.pyplot as plt
xaxis = range(-10,11)
yaxis = []
Bipolar_xaxis= range(-10,11)
Bipolar_yaxis= []
for i in xaxis:
	if i<0:
		f=0
		n=i
	else:
		f=i
		n=0
	yaxis.append(f)
	Bipolar_yaxis.append(n)
	
plt.title("Behaviour of Bipolar ReLU function")
plt.plot(xaxis,yaxis)
plt.plot(Bipolar_xaxis,Bipolar_yaxis)

plt.grid()
plt.show()