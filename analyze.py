import os
import csv
from collections import defaultdict

def analyze_trade_file(base_path, year, month, day):
    file_path = os.path.join(base_path, year, month, day, 'trades.csv')
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No trade file found for {year}/{month}/{day}")

    trades = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            trades.append(row)

    volume_sum = defaultdict(int)
    price_volume_sum = defaultdict(float)

    for trade in trades:
        stock = trade['stock']
        volume = int(trade['volume'])
        price = float(trade['price'])
        volume_sum[stock] += volume
        price_volume_sum[stock] += price * volume

    analysis = []
    for stock in volume_sum:
        total_volume = volume_sum[stock]
        avg_price = price_volume_sum[stock] / total_volume
        analysis.append({
            'stock': stock,
            'total_volume': total_volume,
            'average_price': round(avg_price, 2)
        })

    analysis_path = os.path.join(base_path, year, month, day, f'analysis_{year}{month}{day}.csv')
    with open(analysis_path, 'w', newline='') as csvfile:
        fieldnames = ['stock', 'total_volume', 'average_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in analysis:
            writer.writerow(row)

    return analysis_path
