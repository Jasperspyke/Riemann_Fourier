import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
import time

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

def update_plot(current_sum, iter, term=None):
    plt.style.use('dark_background')
    plt.plot(x, current_sum, color='white', linewidth=2, label='Cumulative Sum')

    square_wave = 1 * (x % (2 * np.pi) < np.pi) - 1 * (x % (2 * np.pi) >= np.pi)
    plt.plot(x, square_wave, color='green', linewidth=2, label='Square Wave')

    if term is not None:
        plt.plot(x, term, color='red', linewidth=2, label='Current Term')

    plt.title(f'Square Wave Series - Iteration: {iter}', fontsize=24)
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.axhline(0, color='white', linewidth=0.8)
    plt.axvline(0, color='white', linewidth=0.8)
    plt.xticks(ticks=np.arange(-2 * np.pi, 3 * np.pi, np.pi),
               labels=[f'{int(t / np.pi)}π' for t in np.arange(-2 * np.pi, 3 * np.pi, np.pi)])

    plt.legend()
    mplcyberpunk.make_lines_glow()
    plt.pause(1)

if __name__ == "__main__":
    sum_curve = np.sin(x)
    update_plot(sum_curve, 0)

    for n in range(3, 10, 2):
        term = (4 / (n * np.pi)) * np.sin(n * x)
        sum_curve += term
        update_plot(sum_curve, n, term)

    plt.show()
