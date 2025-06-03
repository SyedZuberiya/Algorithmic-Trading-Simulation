# Algorithmic Trading Simulation - Moving Average Crossover Strategy

This project simulates a simple algorithmic trading strategy based on the **Moving Average Crossover** technique. It analyzes historical stock price data from a CSV file, generates buy/sell signals, and calculates the resulting profit or loss.

## 📈 Strategy Overview

**Moving Average Crossover Strategy:**
- **Buy Signal:** Triggered when the 50-day moving average (MA50) crosses **above** the 200-day moving average (MA200).
- **Sell Signal:** Triggered when the MA50 crosses **below** the MA200.

This is a momentum-based strategy commonly used in technical analysis.

## 🗂️ Input

A CSV file containing historical stock price data. The CSV must have the following columns:
- `Date` (format: YYYY-MM-DD)
- `Close` (daily closing price)

Example:
```csv
Date,Close
2020-01-01,100.5
2020-01-02,101.2
...
📤 Output
A text or CSV report containing:

Buy and Sell dates with corresponding prices

Net profit/loss from the simulated trades

Trade summary (number of trades, win rate, etc.)

Sample Output
BUY on 2021-03-15 at $125.50
SELL on 2021-07-10 at $138.70
BUY on 2022-01-20 at $142.30
SELL on 2022-05-01 at $130.25

Total Trades: 2
Winning Trades: 1
Losing Trades: 1
Net P/L: $1,105.00
![image](https://github.com/user-attachments/assets/82d678ad-eb13-4ebb-9441-cea424618422)

📁 Files
trading_simulator.py – Main script for simulation.

example.csv – Sample input data.

README.md – Project documentation.
