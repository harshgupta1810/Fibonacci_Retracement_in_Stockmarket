'''
Identify key levels: Start by identifying the high and low points of a recent price trend and draw lines at the key Fibonacci
retracement levels of 23.6%, 38.2%, 50%, 61.8%, and 100%. These levels represent the likely areas where the price may reverse or
 consolidate before continuing in its original direction.

'''

'''
Plot the Fibonacci Levels: Once you have identified the swing high and low, you can plot the Fibonacci retracement levels on the chart. 
You can use the Fibonacci retracement tool available on most trading platforms to do this.

'''

import pandas as pd
import yfinance as yf
from datetime import date
from matplotlib import pyplot as plt


def getdata():
    stocksymbols = 'HDFC.NS'
    ticker = yf.Ticker(stocksymbols)
    end = date.today()
    start = "2020-01-01"
    df = ticker.history(interval="1d", start=start, end=end)
    df.index = df.index.strftime('%d-%m-%y')
    df.index = pd.to_datetime(df.index, format='%d-%m-%y')
    df = df.loc[:, ['Open', 'High', 'Low', 'Close', 'Volume']]
    df = df.round(2)
    return df

def calculate_fibonacci_retracement(df):
    # Calculate Fibonacci levels
    high = df['High']
    low = df['Low']

    # Calculate the highest high and lowest low in the given range
    highest_high = high.max()
    lowest_low = low.min()

    # Calculate the Fibonacci retracement levels
    diff = highest_high - lowest_low
    level_0 = highest_high
    level_23_6 = highest_high - (0.236 * diff)
    level_38_2 = highest_high - (0.382 * diff)
    level_50 = highest_high - (0.5 * diff)
    level_61_8 = highest_high - (0.618 * diff)
    level_100 = lowest_low

    # Add Fibonacci retracement levels to the DataFrame
    dic = {'Fibonacci_0' : level_0,
            'Fibonacci_23.6' : level_23_6,
            'Fibonacci_38.2' : level_38_2,
            'Fibonacci_50' : level_50,
            'Fibonacci_61.8' : level_61_8,
            'Fibonacci_100'  : level_100
           }

    return dic

def plot_fibonacci_levels(fibonacci_level,df):
    # Plot Fibonacci graph
    plot_title = 'Fibonacci Retracement'
    fig = plt.figure(figsize=(22.5, 12.5))
    plt.title(plot_title, fontsize=30)
    ax = fig.add_subplot(111)
    plt.axhline(fibonacci_level['Fibonacci_61.8'], linestyle='--', alpha=0.5, color='purple')
    ax.fill_between(df.index, fibonacci_level['Fibonacci_61.8'], df['Close'].min(), color='purple', alpha=0.2)

    # Fill sections
    plt.axhline(fibonacci_level['Fibonacci_0'], linestyle='--', alpha=0.5, color='blue')
    ax.fill_between(df.index, fibonacci_level['Fibonacci_0'], fibonacci_level['Fibonacci_23.6'], color='blue', alpha=0.2)

    plt.axhline(fibonacci_level['Fibonacci_23.6'], linestyle='--', alpha=0.5, color='green')
    ax.fill_between(df.index, fibonacci_level['Fibonacci_23.6'], fibonacci_level['Fibonacci_38.2'], color='green', alpha=0.2)

    plt.axhline(fibonacci_level['Fibonacci_38.2'], linestyle='--', alpha=0.5, color='red')
    ax.fill_between(df.index, fibonacci_level['Fibonacci_38.2'], fibonacci_level['Fibonacci_50'], color='red', alpha=0.2)

    plt.axhline(fibonacci_level['Fibonacci_50'], linestyle='--', alpha=0.5, color='orange')
    ax.fill_between(df.index, fibonacci_level['Fibonacci_50'], fibonacci_level['Fibonacci_61.8'], color='orange', alpha=0.2)

    plt.axhline(fibonacci_level['Fibonacci_61.8'], linestyle='--', alpha=0.5, color='yellow')
    ax.fill_between(df.index, fibonacci_level['Fibonacci_61.8'], fibonacci_level['Fibonacci_100'], color='brown', alpha=0.2)

    plt.xlabel('Date', fontsize=20)
    plt.show()

