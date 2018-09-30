"""
# Various Elliptic Curve Ploting
# Site: https://stackoverflow.com/questions/19756043/
# python-matplotlib-elliptic-curves
"""
# print(__doc__)


import numpy as np
import matplotlib.pyplot as plt


def plot_elliptic(a=-1, b=1):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    _plot = plt.contour(
        x.ravel(),
        y.ravel(),
        pow(y, 2) - pow(x, 3) - x * a - b,
        [0],
    )
    return _plot

def show_decorated(a, b, title=1, xlabel=1):
    plt.grid()

    if title:
        plt.title("\
            elliptic Curves Depending on a, b\n\
            Y**2 = X**3 + X * a + b")
    if xlabel:
        plt.xlabel("\
            a={0:}, b={1:},\
            Y**2 = X**3 + X * ({0:}) + ({1:})".format(a, b))

def show_some_curves():
    plt.figure(1)

    plt.subplot(211)
    plot_elliptic(-1, 1)
    show_decorated(-1, 1, title=0)

    plt.subplot(212)
    plot_elliptic(-5, 5)
    show_decorated(-5, 5, title=0)

def show_step_b_step_curves():
    # change various a, b  check how graph changes
    for _a in range(-5, 6, 1):
        # _a = [-5 ~ 5] / _b = 1
        plot_elliptic(_a, 1)
        show_decorated(_a, 1, title=0)
        plt.show()

    for _b in range(-5, 6, 1):
        # _a = -1 / _b = [-5 ~ 5]
        plot_elliptic(-1, _b)
        show_decorated(-1, _b, title=0)
        plt.show()

def show_various_curves_comparison():
    plt.figure(1)

    plt.subplot(211)
    for _a in range(-5, 6, 1):
        # _a = [-5 ~ 5] / _b = 0
        plot_elliptic(_a, 0)
    show_decorated(_a, 0, title=0)

    plt.subplot(212)
    for _b in range(-5, 6, 1):
        # _b = [-5 ~ 5] / _a = 0
        plot_elliptic(0, _b)
    show_decorated(0, _b, title=0)



if __name__ == '__main__':
    show_step_b_step_curves()

    show_some_curves()
    plt.show()

    show_various_curves_comparison()
    plt.show()
