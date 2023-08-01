'''
Identify the Swing High and Low: Next, identify the most recent swing high and low points in the trend. The swing high is the highest point in the trend, while the swing low is the lowest point in the trend.

'''


def find_swing_high_low(df):
    swing_highs = []
    swing_lows = []

    for i in range(1, len(df) - 1):
        if (
            df['High'][i] > df['High'][i-1]
            and df['High'][i] > df['High'][i+1]
        ):
            swing_highs.append(df['High'][i])
        else:
            swing_highs.append(None)  # Add None if not a swing high

        if (
            df['Low'][i] < df['Low'][i-1]
            and df['Low'][i] < df['Low'][i+1]
        ):
            swing_lows.append(df['Low'][i])
        else:
            swing_lows.append(None)  # Add None if not a swing low

    swing_highs = [None] + swing_highs + [None]  # Add None for the first and last rows
    swing_lows = [None] + swing_lows + [None]  # Add None for the first and last rows

    for i in range(len(swing_highs)):
        if swing_highs[i] is None:
            swing_highs[i] = swing_highs[i-1]

    for i in range(len(swing_lows)):
        if swing_lows[i] is None:
            swing_lows[i] = swing_lows[i-1]

    df['swing_highs'] = swing_highs
    df['swing_lows'] = swing_lows
    df= df.dropna()
    return df