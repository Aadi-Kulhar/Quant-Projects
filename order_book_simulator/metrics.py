import matplotlib.pyplot as plt

def plot_trades(trades):
    prices, sizes = zip(*trades)
    plt.figure(figsize=(10,4))
    plt.plot(prices, marker='o')
    plt.title('Trade Prices Over Time')
    plt.xlabel('Trade Number')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()
