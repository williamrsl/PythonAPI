from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

app = Flask(__name__);
api = Api(app);

class Users(Resource):
    def get(self):
        return 'William'

api.add_resource(Users, '/users')

if __name__ == "__main__":
    app.run(debug=True)