from flask import Blueprint, request, jsonify
from flask_restplus import Resource, Api, Namespace

api = Namespace('default', description='Create password by default settings')


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        '''
        say hello
        '''
        return {'hello': 'world'}


