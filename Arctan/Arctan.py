from matplotlib import pylab
import pylab as plt
import numpy as np

def tanh(x):
	return (2/(1+np.exp(-2*x)))-1

x_axis = plt.linspace(-10,10)
y_axis = plt.linspace(-1,1)

x = plt.linspace(-10,10,100)

black = (0,0,0)

plt.plot(x, np.arctan(x), 'b', label='Arctan')
plt.plot(x, tanh(x), 'b', label='tanh', color=(1,0,0))


plt.grid()

plt.title('Arctan Cuve')

plt.legend(loc='lower right')

# write the Arctan formula

plt.text(4, 0.8, r'$f(x)=tan^{-1}(x)$', fontsize=15)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()