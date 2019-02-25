from matplotlib import pylab
import pylab as plt
import numpy as np

#sigmoid = lambda x: 1 / (1 + np.exp(-x))
def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def tanh(x):
	return (2/(1+np.exp(-2*x)))-1


x_axis = plt.linspace(-10,10)
y_axis = plt.linspace(-1,1)

x = plt.linspace(-10,10,100)

black = (0,0,0)

plt.plot(x, sigmoid(x), 'b', label='Sigmoid')
plt.plot(x, tanh(x), 'r', label='Tanh')

plt.grid()

plt.title('tanH v/s Sigmoid Function')

plt.legend(loc='lower right')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()