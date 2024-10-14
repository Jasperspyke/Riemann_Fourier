import numpy as np
from scipy.integrate import quad
from scipy.special import expi
from riemann_zeta_zeros import zeros
def li(z):
    return expi(np.log(z))

def mu(n):
    if n == 1: return 1
    if n < 1: return 0

    p, sq = 0, False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p += 1
            if n % (i * i) == 0: sq = True
            while n % i == 0: n //= i
    if n > 1: p += 1
    return 0 if sq else (1 if p % 2 == 0 else -1)

def integrand(z):
    return np.log(z) / (z)

x_interval = np.linspace(1.01, 20, 500)
def riemann_convert(x=x_interval, nth=1):
    a = 1/2
    b = zeros[nth - 1]
    y = np.zeros_like(x, dtype=np.complex_)
    for i in range(len(x)):
        y = np.zeros_like(x, dtype=np.complex_)  # Initialize y as a complex array of the same shape as x

        for n in range(len(x)):
            y[i] += mu(n) * quad(integrand, (a + b * 1j * np.log(x[i])) / n, -np.inf, b)[0]

    return np.real(y)

if __name__ == "__main__":
    print(riemann_convert())