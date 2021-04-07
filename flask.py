from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(name)
api = Api(app)

userss = {
    '1': {
        'name': 'van',
        'age': '30'
    },
    '2': {
        'name': 'billy',
        'age': '33'
    },
    '3': {
        'name': 'max',
        'age': '99'
    }
}

class Users(Resource):
    def get(self):
        return {'data': userss}, 200

api.add_resource(Users, '/users')

if name == 'main':
    app.run()
