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
        return json.load(open('ratios.json', 'r'))


class Industries(Resource):

    def get(self):
        return json.load(open('by-industry.json', 'r'))


api.add_resource(AllRates, '/all-rates/')
api.add_resource(Industries, '/industries/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
