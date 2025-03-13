import requests
from binance.client import Client
from flask import Flask, render_template
import config

app = Flask(__name__)

# Function to get the current price of a cryptocurrency from CoinGecko
def get_crypto_price(crypto_id='bitcoin', currency='usd'):
    # Build the API URL to request the price of a specific cryptocurrency
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}'
    response = requests.get(url)
    data = response.json()
    
    # Get the price from the returned data
    price = data.get(crypto_id, {}).get(currency)
    
    if price:
        return price
    else:
        # Raise an error if the price cannot be fetched
        raise ValueError(f"Could not fetch the price for {crypto_id}")

# Function to get mining statistics from NiceHash
def get_mining_stats(api_key, user_id):
    # Build the URL to request the mining statistics
    url = f'https://api2.nicehash.com/api/v2/stats/summary/{user_id}'
    headers = {
        'X-Time': 'time',
        'X-API-Key': api_key
    }
    
    # Make the request and return the statistics
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# Function to trade cryptocurrency for stablecoin on Binance
def trade_crypto_to_stablecoin(api_key, api_secret, crypto_amount, symbol='BTCUSDT'):
    # Initialize the Binance client using the API keys
    client = Client(api_key, api_secret)
    
    # Get the current market price of the cryptocurrency to trade
    price = client.get_symbol_ticker(symbol=symbol)['price']
    price = float(price)
    
    # Calculate the stablecoin amount based on the amount of crypto mined
    stablecoin_amount = crypto_amount * price
    
    # Execute a market sell order to exchange crypto for stablecoin (USDT)
    order = client.order_market_sell(
        symbol=symbol,  # Symbol for the exchange (BTC -> USDT)
        quantity=crypto_amount
    )
    
    return order, stablecoin_amount, price

# Web page route to display the mining statistics and exchange results
@app.route('/')
def index():
    # Get the current price of Bitcoin from CoinGecko
    crypto_price = get_crypto_price(config.CRYPTO_ID, 'usd')
    
    # Get mining statistics from NiceHash API
    mining_stats = get_mining_stats(config.NICEHASH_API_KEY, config.NICEHASH_USER_ID)
    
    # Replace 'your_mining_stat' with the actual mining statistics key from the NiceHash response
    crypto_amount = mining_stats.get('your_mining_stat', {}).get('value', 0)  # Example: mined Bitcoin amount

    # Exchange the mined cryptocurrency for stablecoin using Binance API
    order, stablecoin_amount, price = trade_crypto_to_stablecoin(config.BINANCE_API_KEY, config.BINANCE_API_SECRET, crypto_amount)
    
    # Render the web page with the mining and exchange results
    return render_template('index.html', crypto_price=crypto_price, crypto_amount=crypto_amount, stablecoin_amount=stablecoin_amount, price=price)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
