import numpy as np
from order_book import OrderBook

class AgentSimulator:
    def __init__(self, book, num_steps=1000):
        self.book = book
        self.num_steps = num_steps

    def simulate(self):
        for _ in range(self.num_steps):
            side = np.random.choice(['buy', 'sell'])
            price = round(np.random.normal(100, 2), 2)
            quantity = np.random.randint(1, 10)
            self.book.add_order(side, price, quantity)
            self.book.match()
