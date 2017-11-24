from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
from flask_cors import CORS
from models import Stock
from database import db_session


app = Flask(__name__)

parser = reqparse.RequestParser()
parser.add_argument('ticker', location='args')
parser.add_argument('price', location='args')


@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>INDEX</title>
        </head>
       <body>
           <a href="/all-rates/">HERE</a>
       </body>
    </html>
    """

api = Api(app)
CORS(app)


class AllRates(Resource):
    def get(self):
        return json.load(open('json-data/ratios.json', 'r'))


class Companies(Resource):
    def get(self):
        return json.load(open('json-data/companies.json', 'r'))


# curl 'http://localhost:5000/price/?ticker=MSFT'
class Price(Resource):
    def get(self):
        price = 0
        args = parser.parse_args()
        # ticker = args['ticker']
        for p, in db_session.query(Stock.price). \
                filter(Stock.ticker == 'AAPL'):
            price = p

        return 'success: ' + ' ' + str(price)


# curl -X PUT 'http://localhost:5000/set-price/?ticker=MSFT&price=42'
class SetPrice(Resource):
    def get(self):
        # args = parser.parse_args()
        # ticker = args['ticker']
        # price = args['price']
        price = Stock(ticker='AAPL', price=10.5)
        db_session.add(price)
        db_session.commit()
        return 'success: ' + 'AAPL' + ' ' + str(price.price)


api.add_resource(Companies, '/companies/')
api.add_resource(AllRates, '/all-rates/')
api.add_resource(Price, '/price/')
api.add_resource(SetPrice, '/set-price/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
