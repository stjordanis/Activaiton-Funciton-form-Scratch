from matplotlib import pylab
import pylab as plt
import numpy as np

#sigmoid = lambda x: 1 / (1 + np.exp(-x))
def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

x_axis = plt.linspace(-10,10)
y_axis = plt.linspace(-1,1)

x = plt.linspace(-10,10,100)

black = (0,0,0)

plt.plot(x, sigmoid(x), 'b', label='Sigmoid')

plt.grid()

plt.title('Sigmoid Function')

plt.legend(loc='lower right')

# write the Sigmoid formula
plt.text(4, 0.8, r'$\sigma(x)=\frac{1}{1+e^{-x}}$', fontsize=15)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()