import backtrader as bt
from oanda_data import fetch_oanda_data
from ict_strategy import ICTStrategy

# Fetch data
data_df = fetch_oanda_data(api_key="your_real_api_key")

# Backtrader setup
bt_data = bt.feeds.PandasData(dataname=data_df)
cerebro = bt.Cerebro()
cerebro.adddata(bt_data)
cerebro.addstrategy(ICTStrategy)
cerebro.run()
cerebro.plot()
print("Backtest complete.")
cerebro.plot()

