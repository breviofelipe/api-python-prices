from flask import Flask, request
from yahoofinancials import YahooFinancials
from flask import jsonify

app = Flask(__name__)

@app.route('/current_price')
def get_current_price():
    ticker = request.args.get('ticker')
    yahoo_financials = YahooFinancials(ticker)
    response = yahoo_financials.get_current_price()   
    return jsonify(response)


if __name__ == '__main__':
    app.run()