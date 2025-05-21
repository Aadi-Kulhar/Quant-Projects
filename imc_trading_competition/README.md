# IMC Trading Competition – Market Making & Arbitrage Strategies

This repository contains my solo solutions to the IMC Trading Competition (2024). It includes two primary strategies:

- **Market Making Engine** with inventory-aware quoting and dynamic spread adjustment
- **Cross-Product Arbitrage Bot** for mispriced synthetic baskets (e.g., PICNIC_BASKET1)

## Features

- Inventory-sensitive quote placement using RSI/Bollinger signals
- Synthetic product decomposition and arbitrage execution
- Queue position estimation and fair value calculation
- Real-time PnL tracking, order book updates, and risk management

## Structure

```
imc_trading_competition/
├── strategies/
│   ├── market_maker.py
│   ├── arbitrage_engine.py
│   └── utils.py
├── simulator/
│   └── exchange_env.py
├── results/
│   └── trades_log.csv
├── config.json
├── main.py
└── README.md
```

## Run

```bash
python main.py
```

This was submitted as a solo entry and placed in the top percentile globally.
