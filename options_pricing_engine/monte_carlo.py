import numpy as np

def monte_carlo_price(S, K, T, r, sigma, simulations=100000, option_type='call'):
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2)*T + sigma*np.sqrt(T)*Z)
    if option_type == 'call':
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)
    price = np.exp(-r*T) * np.mean(payoff)
    return price
