from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
from flask_cors import CORS
from redis import Redis


redis = Redis(host='redis', port=6379, db=0)
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


class Price(Resource):
    def get(self):
        a = redis.get('HPE')
        return str(a)


class SetPrice(Resource):
    def put(self):
        args = parser.parse_args()
        ticker = args['ticker']
        price = args['price']
        redis.set(ticker, price)
        return 'success: ' + ticker + ' ' + price


api.add_resource(Companies, '/companies/')
api.add_resource(AllRates, '/all-rates/')
api.add_resource(Price, '/price/')
api.add_resource(SetPrice, '/set-price/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
