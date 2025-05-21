import heapq

class Order:
    def __init__(self, order_id, side, price, quantity):
        self.order_id = order_id
        self.side = side  # 'buy' or 'sell'
        self.price = price
        self.quantity = quantity

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # max-heap
        self.sell_orders = []  # min-heap
        self.order_id = 0
        self.trades = []

    def add_order(self, side, price, quantity):
        order = Order(self.order_id, side, price, quantity)
        self.order_id += 1
        if side == 'buy':
            heapq.heappush(self.buy_orders, (-price, self.order_id, order))
        else:
            heapq.heappush(self.sell_orders, (price, self.order_id, order))
        return order.order_id

    def match(self):
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0][2]
            best_sell = self.sell_orders[0][2]
            if -self.buy_orders[0][0] >= self.sell_orders[0][0]:
                trade_qty = min(best_buy.quantity, best_sell.quantity)
                self.trades.append((best_buy.price, trade_qty))
                best_buy.quantity -= trade_qty
                best_sell.quantity -= trade_qty

                if best_buy.quantity == 0:
                    heapq.heappop(self.buy_orders)
                if best_sell.quantity == 0:
                    heapq.heappop(self.sell_orders)
            else:
                break
