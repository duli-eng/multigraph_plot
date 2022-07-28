#!/usr/bin/env python3
# plot_parabola.py

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    x = np.linspace(-4, 5, 100)
    y = np.power(x,2) + 1

    # Step 1 - Plot the graph on the main axes
    ax.plot(x, y)

    # Step 2 - Give the graph a title and axis labels
    ax.set_title("$y = x^2+1$")  # LaTeX format
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Step 3 - Center the graph on appropriate range
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 30)

    # Step 4 - Turn on the grid, and add decorations
    ax.grid()
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.plot(0, 1, color='red', marker='o')
    ax.axhline(1, color='blue', linestyle='--')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()