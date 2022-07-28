#!/usr/bin/env python3
# plot_rings.py

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    radius = 25
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    x_offset = 5/2 * radius
    y_offset = radius

    ax.plot(x, y, color='black', linewidth=10)
    ax.plot(x + x_offset, y, color='red', linewidth=10)
    ax.plot(x - x_offset, y, color='blue', linewidth=10)
    ax.plot(x - x_offset / 2, y - y_offset, color='yellow', linewidth=10)
    ax.plot(x + x_offset / 2, y - y_offset, color='green', linewidth=10)

    ax.set_title("The Olympic Rings")
    ax.set_aspect('equal')
    ax.axis('off')


def main():
    fig = plt.figure()
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
