import numpy as np
import math
import matplotlib.pyplot as plt


def psi_k(x, g_range):
    print("A")
    k = 6*math.pi/10
    len_g_range = len(g_range)
    return_val = 0
    for m in range(len_g_range):
        g_val = g_range[m]
        return_val += (.02/(m+1)*np.exp(-1j*(k-g_val)*x))
    return return_val


if __name__ == "__main__":
    print("working")
    x_values = np.arange(0, 10, .01)
    G_range = np.arange(-8*np.pi, +8*np.pi, 2*np.pi)
    plt.figure(1)
    plt.plot(x_values, np.real(psi_k(x_values, G_range)))
    plt.show()
