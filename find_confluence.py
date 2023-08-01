
'''
Look for confluence: Look for confluence between the Fibonacci retracement levels and other support and resistance levels such as round numbers or previous price highs or lows. This can increase the likelihood of a reversal or consolidation at that level.

'''

import numpy as np


def find_confluence(df):
    # Calculate Fibonacci retracement levels
    price_high = df['High'].max()
    price_low = df['Low'].min()
    price_range = price_high - price_low

    fibonacci_levels = [0.236, 0.382, 0.5, 0.618, 0.786]
    fib_levels = []
    for level in fibonacci_levels:
        fib_levels.append(price_high - level * price_range)

    # Look for confluence between Fibonacci levels and other levels
    confluence_levels = []
    for level in fib_levels:

        # Previous price high/low confluence
        if df['swing_highs'].max() >= level >= df['swing_lows'].min():
            confluence_levels.append(level)

    return np.unique(confluence_levels)
