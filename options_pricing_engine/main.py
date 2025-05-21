import yfinance as yf
from black_scholes import black_scholes_price
from monte_carlo import monte_carlo_price
from greeks import black_scholes_greeks
from visualization import plot_vol_surface

ticker = 'AAPL'
stock = yf.Ticker(ticker)
data = stock.history(period='1d')
S = data['Close'][-1]
K = round(S * 1.05, 2)
T = 30 / 365
r = 0.05
sigma = 0.25

print(f"Live AAPL Price: {S:.2f}")
print("\n--- Black-Scholes ---")
bs_price = black_scholes_price(S, K, T, r, sigma)
print(f"Call Option Price (BS): {bs_price:.2f}")

print("\n--- Monte Carlo ---")
mc_price = monte_carlo_price(S, K, T, r, sigma)
print(f"Call Option Price (MC): {mc_price:.2f}")

print("\n--- Greeks ---")
greeks = black_scholes_greeks(S, K, T, r, sigma)
for g, val in greeks.items():
    print(f"{g.capitalize()}: {val:.4f}")

print("\n--- Volatility Surface ---")
plot_vol_surface(S, r)
