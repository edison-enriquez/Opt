from sympy import *

x, y = symbols("x y")
f = (input("function f(x,y):"))

derx = diff(f,x)

print(f'df_x(x) = {derx}')
