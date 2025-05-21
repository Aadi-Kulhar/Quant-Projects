import numpy as np

def historical_var(returns, confidence=0.95):
    return -np.percentile(returns, (1 - confidence) * 100)

def parametric_var(returns, confidence=0.95):
    mean = np.mean(returns)
    std = np.std(returns)
    z = np.abs(np.percentile(np.random.normal(0, 1, 100000), (1 - confidence) * 100))
    return -(mean + z * std)

def monte_carlo_var(S0, mu, sigma, T=1, confidence=0.95, simulations=10000):
    np.random.seed(0)
    Z = np.random.standard_normal(simulations)
    ST = S0 * np.exp((mu - 0.5 * sigma**2)*T + sigma * np.sqrt(T) * Z)
    returns = (ST - S0) / S0
    return -np.percentile(returns, (1 - confidence) * 100)

def cvar(returns, confidence=0.95):
    var = historical_var(returns, confidence)
    return -np.mean([r for r in returns if r < -var])
