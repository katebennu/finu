from flask import Flask
from flask_restful import Resource, Api
import json
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class AllRates(Resource):

    def get(self):
        return json.load(open('ratios.json', 'r'))


api.add_resource(AllRates, '/all-rates/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
