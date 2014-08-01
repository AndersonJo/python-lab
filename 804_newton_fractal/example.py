'''
Created on 2014. 8. 2.

@author: a141890
'''

from matplotlib.pyplot import plot, show
from numpy import pi, cos, sin

solutions = [cos((2*n+1)*pi/4)+1j*sin((2*n+1)*pi/4) for n in range(4)]

print solutions

plot(solutions)
show()