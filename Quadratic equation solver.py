import matplotlib.pyplot as plt
import numpy as np


a = input("what is the coefficient for x^2, a: ")
b = input("what is the coefficient for x, b: ")
c = input("what is the constant, c: ")

a = float(a)
b = float(b)
c = float(c)

x1 = -b/(2*a) + ((b**2-4*a*c)**(1/2))/(2*a)
x2 = -b/(2*a) - ((b**2-4*a*c)**(1/2))/(2*a)
if b**2-4*a*c >= 0:
    print(a,b,c)
    print(x1)
    print(x2)
    x = np.linspace(-5, 5, 100)
    y = a * x ** 2 + b * x + c

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')

    plt.show()
else:
    print("there are no real roots to this equation")

    x = np.linspace(-5, 5, 100)

    y = a * x ** 2 + b * x + c

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.title("No real roots")

    plt.plot(x, y, 'r')

    plt.show()










