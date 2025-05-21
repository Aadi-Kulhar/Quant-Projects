from order_book import OrderBook
from agent_simulator import AgentSimulator
from metrics import plot_trades

book = OrderBook()
simulator = AgentSimulator(book, num_steps=500)
simulator.simulate()

print(f"Executed Trades: {len(book.trades)}")
plot_trades(book.trades)
