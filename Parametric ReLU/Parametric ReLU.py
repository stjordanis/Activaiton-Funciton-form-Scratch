import math
import matplotlib.pyplot as plt
xaxis = range(-10,11)
yaxis = []
alpha = 0.5
for i in xaxis:
	if i<0:
		f=i*alpha
	else:
		f=i
	yaxis.append(f)

plt.text(7.5, -4, r'$\alpha =0.5$', fontsize=15)
plt.title("Behaviour of Parametric ReLU function")
plt.plot(xaxis,yaxis)
plt.grid()
plt.show()