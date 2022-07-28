#!/usr/bin/env python3
# plot_rose_curves.py

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    theta = np.linspace(0, 4 * np.pi, 1000)

    radius_1 = 4 + 4 * np.cos(4 * theta)
    radius_2 = 3 + 3 * np.cos(4 * theta + np.pi)
    radius_3 = 5 + 5 * np.cos(3 / 2 * theta)
    radius_4 = 7 + 2 * np.cos(5 * theta) * np.sin(11 * theta)

    ax.plot(theta, radius_1, color='blue')
    ax.plot(theta, radius_2, color='green')
    ax.plot(theta, radius_3, color='red')
    ax.plot(theta, radius_4, color='purple')

    ax.set_aspect('equal')
    ax.axis()


def main():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
