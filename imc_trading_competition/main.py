from strategies.market_maker import run_market_maker
from strategies.arbitrage_engine import run_arbitrage

if __name__ == '__main__':
    print("Running Market Making Strategy...")
    run_market_maker()

    print("\nRunning Arbitrage Strategy...")
    run_arbitrage()
