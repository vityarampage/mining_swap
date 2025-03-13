# Crypto Mining Auto-Exchange Bot

A Python-based automated system that monitors cryptocurrency mining earnings, retrieves live market prices, and automatically exchanges mined cryptocurrency (e.g., Bitcoin) to stablecoins (e.g., USDT) using Binance.

## Features

- **Automated Mining Monitoring**: Fetches mining statistics from NiceHash API.
- **Real-time Crypto Prices**: Uses CoinGecko API to retrieve the latest cryptocurrency prices.
- **Automatic Crypto Exchange**: Automatically exchanges mined crypto to stablecoins on Binance.
- **User Dashboard**: Displays mining stats, crypto prices, and transaction details via a Flask web interface.

## Project Structure

```
crypto-mining-bot/
├── app.py              # Main Flask application
├── config.py           # API keys and configuration
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML for the web interface
└── static/
    └── style.css       # CSS styling for the dashboard
```

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Binance account with API access
- NiceHash account with API access

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/crypto-mining-bot.git
cd crypto-mining-bot
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure API keys and settings in `config.py`:

```python
# config.py
BINANCE_API_KEY = 'your_binance_api_key'
BINANCE_API_SECRET = 'your_binance_api_secret'
NICEHASH_API_KEY = 'your_nicehash_api_key'
NICEHASH_USER_ID = 'your_nicehash_user_id'
CRYPTO_ID = 'bitcoin'
STABLECOIN_SYMBOL = 'BTCUSDT'
```

## Running the Application

1. Start the Flask app:

```bash
python app.py
```

2. Open your browser and visit:

```
http://127.0.0.1:5000/
```

## Usage

1. Monitor real-time mining statistics from NiceHash.
2. View the current price of your mined cryptocurrency.
3. Automatically convert mined crypto to stablecoins (BTC to USDT).

## Environment Variables (Optional)

Alternatively, you can use environment variables for sensitive information:

```bash
export BINANCE_API_KEY='your_api_key'
export BINANCE_API_SECRET='your_api_secret'
export NICEHASH_API_KEY='your_nicehash_key'
export NICEHASH_USER_ID='your_nicehash_user_id'
```

## Dependencies

- Flask (for web interface)
- Requests (for API calls)
- python-binance (for interacting with Binance)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Notes

- Ensure your Binance account has trading enabled.
- Adjust the crypto and stablecoin symbols in `config.py` as needed.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Feel free to fork the repository and open a pull request.

## Troubleshooting

- Ensure your API keys have the correct permissions.
- Check the Flask server logs for any errors during execution.
- Confirm the Binance trading pair exists (e.g., BTCUSDT).

## Future Enhancements

- Support for additional mining platforms (e.g., HiveOS, Ethermine).
- Detailed logging and notification system.
- Docker support for easier deployment.

