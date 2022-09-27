import numpy as np

def f(x):
    return x**x - 100

def Df(x):
    return x**x(np.log(x)+1)

x0 = 1

for i in range(1,11):
    x1=x0 -f(x0) / Df(x0)
    x0 = x1
    print(f'Iter: {x1}, srqt aprox = {x0}')
