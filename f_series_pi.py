import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from scipy import integrate
from harmonics import riemann_harmonic

x = np.linspace(1.01, 20, 10000)

def li_integrand(t):
    return 1 / np.log(t)

def li(x):
    return integrate.quad(li_integrand, 2, x)[0] + 1.045163 if x > 2 else 0

def pi(x):
    return np.array([np.sum(1 for i in range(2, int(t) + 1) if all(t % j != 0 for j in range(2, int(t) // 2 + 1))) for t in x])

li_values = np.array([li(t) for t in x])
pi_values = pi(x)
pi_values[-1] = pi_values[-2]

def update_plot(current_sum, iter, term=None):
    plt.style.use('dark_background')
    plt.plot(x, current_sum, color='white', linewidth=2, label='Cumulative Sum')

    if term is not None:
        plt.plot(x, term, color='red', linewidth=2, label=f'Term {iter}')

    if iter == 0:
        plt.plot(x, li_values, color='cyan', linewidth=2, label='Li(x)')

    plt.step(x, pi_values, where='post', color='green', linewidth=2, label='π(x)')
    plt.title(f'Li(x) Fourier Series - Iteration: {iter}', fontsize=24)
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.axhline(0, color='white', linewidth=0.8)
    plt.axvline(0, color='white', linewidth=0.8)
    plt.xticks(np.arange(1, 21, 1))
    plt.legend()
    mplcyberpunk.make_lines_glow()
    plt.pause(1)

if __name__ == "__main__":
    sum_curve = li_values.copy()
    update_plot(sum_curve, 0)

    for n in range(1, 6):
        term = riemann_harmonic(x, n) / n
        sum_curve += term
        update_plot(sum_curve, n, term)

    plt.show()
