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


def main(a=-1, b=1):
    plot_elliptic(a, b)
    plt.grid()
    plt.title("\
        elliptic Curves Depending on a, b\n\
        Y**2 = X**3 + X * a + b")
    plt.xlabel("\
        a={0:}, b={1:},\
        Y**2 = X**3 + X * ({0:}) + ({1:})".format(a, b))
    plt.show()


if __name__ == '__main__':
    plt.figure(1)

    plt.subplot(211)
    for _a in range(-5, 6, 1):
        # _a = [-5 ~ 5] / _b = 0
        plot_elliptic(_a, 0)

    plt.grid()
    plt.xlabel("\
        a=-5 ~ 5, b=0,\
        Y**2 = X**3 + X * ({0:}) + ({1:})".format(_a, 0))


    plt.subplot(212)
    for _b in range(-5, 6, 1):
        # _b = [-5 ~ 5] / _a = 0
        plot_elliptic(0, _b)

    plt.grid()
    plt.xlabel("\
        a=0, b=-5 ~ 5,\
        Y**2 = X**3 + X * ({0:}) + ({1:})".format(0, _b))

    plt.show()



    # # change various a, b  check how graph changes
    # for _a in range(-5, 6, 1):
    #     # _a = [-5 ~ 5] / _b = 1
    #     main(_a)
    #
    # for _b in range(-5, 6, 1):
    #     # _a = -1 / _b = [-5 ~ 5]
    #     main(-1, _b)

    # plt.figure(1)
    #
    # plt.subplot(211)
    # plot_elliptic(-1,1)
    # plt.grid()
    #
    # plt.subplot(212)
    # plot_elliptic(-5,5)
    # plt.grid()
    # plt.show()
