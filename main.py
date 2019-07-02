import numpy as np
import matplotlib.pyplot as plt
from IPython import display


def target_fun(x):
    y = x * np.sin(x * np.pi * 10) + 2
    return y;


if __name__ == '__main__':
    plt.show([])