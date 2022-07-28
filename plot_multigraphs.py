#!/usr/bin/env python3
# plot_multigraphs.py

import matplotlib.pyplot as plt

import plot_parabola
import plot_polynomial
import plot_rings
import plot_rose_curves


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2)

    ax = fig.add_subplot(gs[0, 0])
    plot_rings.plot(ax)

    ax = fig.add_subplot(gs[0, 1], projection='polar')
    plot_rose_curves.plot(ax)

    ax = fig.add_subplot(gs[1, 0])
    plot_parabola.plot(ax)

    ax = fig.add_subplot(gs[1, 1])
    plot_polynomial.plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
