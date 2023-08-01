'''
Identifying potential entry and exit points: Traders use Fibonacci retracements to identify potential levels of support and resistance in a stock's price trend. These levels can be used to identify potential entry and exit points for trades.

'''

def identify_entry_exit_points(df):
    # Calculate Fibonacci levels
    high = df['High'].max()
    low = df['Low'].min()
    diff = high - low

    fib_levels = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
    fib_values = [low + level * diff for level in fib_levels]

    # Identify swing highs and swing lows
    df.loc[:, 'IsSwingHigh'] = df['High'] > df['High'].shift(1)
    df.loc[:, 'IsSwingLow'] = df['Low'] < df['Low'].shift(1)

    # Filter swing highs and swing lows
    swing_highs = df.loc[df['IsSwingHigh'], 'High']
    swing_lows = df.loc[df['IsSwingLow'], 'Low']

    # Identify potential entry and exit points
    df['entry_points'] = swing_highs[swing_highs <= fib_values[3]]
    df['exit_points'] = swing_lows[swing_lows >= fib_values[3]]
    df.fillna(method='ffill', inplace=True)
    df = df.fillna(0)
    return df