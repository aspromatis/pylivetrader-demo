# Live RSI Momentum Trading with pylivetrader

Use the RSI signal to drive algorithm buying and selling decisions. When the RSI is over 70, a stock is considered overbought and is sold (or shorted). On the other hand, when the RSI is below 30, a stock is considered oversold and is bought.
Here is additional information from [Investorpedia](https://www.investopedia.com/terms/r/rsi.asp).

## Create and set-up a new virtual environment in Conda

Download and install [Anaconda](https://www.anaconda.com/products/individual)

Create a new environment in your conda navigator or terminal and use Python version 3.6 given dependencies.

`$ conda create -n ziplive36 python=3.6`

Activate the new environment.

`$ conda activate ziplive36`

Install [pylivetrader](https://github.com/alpacahq/pylivetrader)

`pip install pylivetrader`

Install the [Python wrapper](https://github.com/mrjbq7/ta-lib) for [TA-Lib](https://www.ta-lib.org/)

`$ pip install TA-Lib`

## Supported Brokers

Alpaca

Configuration by environment variables.

`$ export APCA_API_KEY_ID={your api key id}`
`$ export APCA_API_SECRET_KEY={your api secret key}`
`$ export APCA_API_BASE_URL={https://api.alpaca.markets/ or https://paper-api.alpaca.markets}`
`$ pylivetrader run -f algo.py`

Configuration by config file. Either yaml or json.

`$ cat config.yaml`
`key_id: {your api key id}`
`secret: {your api secret key}`
`base_url: {https://api.alpaca.markets/ or https://paper-api.alpaca.markets}`
`$ pylivetrader run -f algo.py --backend-config config.yaml`



Disclaimer - This is just a demo algo and using it 'as is' carries significant financial risk, so don't use it.  All code and content is for educational purposes only and is not financial advice.
