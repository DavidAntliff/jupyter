import numpy as np


def get_x(n=100):
    return np.linspace(0, 2 * np.pi, n)


def get_cos(x, A=1, f=1):
    return A * np.cos(x * f)
