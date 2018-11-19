import numpy as np
import math
import matplotlib.pyplot as plt


def psi_k(c, k, x, g_range):
    len_g_range = len(g_range)
    return_val = 0
    for m in range(len_g_range):
        if m != 0:
            return_val += (c/(m+1)*np.exp(1j*(k-g_range[m])*x))
            return_val += (c/(m+1)*np.exp(1j*(k+g_range[m])*x))
        else:
            return_val += (c/(m+1)*np.exp(1j*(k-g_range[m])*x))

    return return_val


def u_k(c, x, g_range):
    len_g_range = len(g_range)
    return_val = 0
    for m in range(len_g_range):
        return_val += (c/(m+1)*np.exp(1j*(g_range[m])*x))
        return_val += (c/(m+1)*np.exp(1j*(g_range[m])*x))
    else:
        return_val += (c/(m+1)*np.exp(1j*(g_range[m])))

    return return_val


if __name__ == "__main__":
    k_val = 4 * math.pi / 10
    c_values = [.05, .2, .4, 1, 10, 100]
    x_values = np.arange(0, 10, .01)
    G_range = np.arange(0, +8*np.pi, 2*np.pi)

    num_cvals = len(c_values)
    fig, axs = plt.subplots(nrows=num_cvals, ncols=3)
    for i in range(num_cvals):
        ax = axs[i, 0]
        ax.plot(x_values, np.real(psi_k(c_values[i], k_val, x_values, G_range)))

        ax = axs[i, 1]
        ax.plot(x_values, np.conj(psi_k(c_values[i], k_val, x_values, G_range))*psi_k(c_values[i], k_val, x_values, G_range))

        ax = axs[i, 2]
        ax.plot(x_values, np.real(u_k(c_values[i], x_values, G_range)))

    plt.show()
