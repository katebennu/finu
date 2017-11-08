from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class AllRates(Resource):
    def get(self):
        return json.load(open('ratios.json', 'r'))


api.add_resource(AllRates, '/')

if __name__ == '__main__':
    app.run(debug=True)
