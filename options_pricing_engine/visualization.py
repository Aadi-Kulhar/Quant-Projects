import matplotlib.pyplot as plt
import numpy as np
from black_scholes import black_scholes_price

def plot_vol_surface(S, r, option_type='call'):
    T = np.linspace(0.1, 2.0, 20)
    K = np.linspace(0.8*S, 1.2*S, 20)
    T_grid, K_grid = np.meshgrid(T, K)
    sigma = 0.2

    Z = np.vectorize(lambda k, t: black_scholes_price(S, k, t, r, sigma, option_type))(K_grid, T_grid)

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(K_grid, T_grid, Z, cmap='viridis')
    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Time to Maturity')
    ax.set_zlabel('Option Price')
    ax.set_title('Black-Scholes Volatility Surface')
    plt.show()
