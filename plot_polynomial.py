#!/usr/bin/env python3
# plot_polynomial.py

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Poly, real_roots, Derivative, lambdify, latex


def plot(ax):

    x = symbols('x')

    # fn(x) = 2x^3 - 2x^2 - 11x + 52
    fn = Poly([1, -2, -120, 52, 2119, 1980], x)

    fn_zeros = np.asarray([np.float(r) for r in real_roots(fn)])

    fn_d1 = Derivative(fn, x, evaluate=True)
    fn_d1_zeros = np.asarray([np.float(r) for r in real_roots(fn_d1)])

    x_pts = np.sort(np.concatenate((fn_zeros, fn_d1_zeros)))

    x_min, x_max = x_pts[0] - 1, x_pts[-1] + 1
    print(f"x_min = {x_min:.4f}, x_max = {x_max:.4f}")

    xa = np.linspace(x_min, x_max, 1000)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')

    fn_lambda = lambdify(x, fn.as_expr(), modules='numpy')

    ax.plot(xa, fn_lambda(xa), linewidth=2)

    ax.grid()
    ax.scatter(fn_zeros, fn_lambda(fn_zeros), color='red')
    ax.scatter(fn_d1_zeros, fn_lambda(fn_d1_zeros), color='orange')

    ax.set_title(f"$y = {latex(fn.as_expr())}$")


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
