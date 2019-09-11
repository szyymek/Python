from sympy import *
from sympy.plotting import plot, plot_parametric

expr = sin(2*sin(x**3))
plot(expr, (x,0,5))
