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


class AllCompanies(Resource):
    def get(self):
        return


class RatesSet(Resource):
    def get(self):
        return


class StatementSet(Resource):
    def get(self):
        return


class Company(Resource):
    def get(self):
        return json.load(open('json-data/companies.json', 'r'))

    def post(self):
        return


class Entry(Resource):
    def get(self):
        return

    def put(self):
        return


# curl 'http://localhost:5000/price/?ticker=MSFT'
class Price(Resource):
    def get(self):
        args = parser.parse_args()
        price = 0
        ticker = args['ticker']
        stock = db_session.query(Stock.price).filter_by(ticker=ticker).first()
        price = stock.price
        return 'success! ' + ticker + ' ' + str(price)

# curl -X PUT 'http://localhost:5000/set-price/?ticker=MSFT&price=42'
    def put(self):
        args = parser.parse_args()
        ticker = args['ticker']
        price = args['price']
        stock = db_session.query(Stock).filter_by(ticker=ticker).first()
        from pprint import pprint
        pprint(stock)
        if stock:
            stock.price = price
        else:
            stock = Stock(ticker=ticker, price=float(price))
            db_session.add(stock)
        db_session.commit()
        return 'success: ' + ticker + ' ' + str(stock.price)




api.add_resource(AllRates, '/all-rates/')
api.add_resource(AllCompanies, '/companies/')
api.add_resource(RatesSet, '/rates-set/')
api.add_resource(StatementSet, '/statement-set/')
api.add_resource(Company, '/company/')
api.add_resource(Entry, '/entry/')
api.add_resource(Price, '/price/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
