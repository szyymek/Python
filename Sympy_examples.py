from sympy import *
from sympy.plotting import plot, plot_parametric

expr = [sin(2*sin(x**3)), sin(x), cos(x)]
for funkcja in expr:
    plot(funkcja, (x,0,5))
