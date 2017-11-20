from flask import Flask
from flask_restful import Resource, Api
import json
from flask_cors import CORS

app = Flask(__name__)


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


api.add_resource(Companies, '/companies/')
api.add_resource(AllRates, '/all-rates/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
