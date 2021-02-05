
import talib
from pylivetrader.api import order_target, symbol, order_target_percent, order_target_value

def initialize(context):
    context.i = 0
    
    # what stock to trade - FAANG in this example
    stocklist = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']

    # make a list of symbols for the list of tickers
    context.stocks = [symbol(s) for s in stocklist]
    
    # create equal weights of each stock to hold in our portfolio
    context.target_pct_per_stock = 1.0 / len(context.stocks)
    
    # create initial RSI threshold values for low (oversold and buy signal) and high (overbought and sell signal)
    context.LOW_RSI = 30
    context.HIGH_RSI = 70

def handle_data(context, data):
    
    print('handle data')
    
    # Load historical pricing data for the stocks, using specified (1d or 1m, etc.) frequncy and a rolling 20 periods (i.e. minuted, days, etc)
    prices = data.history(context.stocks, 'price', bar_count=20, frequency="1m")  #I'm using 1m for this demo so that you can see the trades working on Alpaca
    
    # initialize a new variable to hold the rsi values
    rsis = {}
        
    # Loop through our list of stocks
    for stock in context.stocks:
        # Get the rsi of this stock.
        rsi = talib.RSI(prices[stock], timeperiod=14)[-1]
        rsis[stock] = rsi
        
        current_position = context.portfolio.positions[stock].amount
        
        # for testing, print out some of the variables
        print('stock: ' + str(stock) + ' price: ' + str(data.current(stock, "price")) + ' rsi: ' + str(rsi) + ' position: ' + str(current_position))
        
        # RSI is above 70 and we own shares, time to sell
        if rsi > context.HIGH_RSI and current_position >= 0 and data.can_trade(stock):
            order_target(stock, -10)
            print('SHORT')
   
        # RSI is below 30 and we don't have any shares, time to buy
        elif rsi < context.LOW_RSI and current_position == 0 and data.can_trade(stock):
            order_target(stock, 10)  # You can also use different and more complex order type functions
            print('LONG')


