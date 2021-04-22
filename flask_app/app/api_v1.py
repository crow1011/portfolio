from flask import Blueprint
from flask_restplus import Api
from apis.pwdgen_endpoint import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
    title='Password Generator',
    version='1.0',
    description='Create safe password'
)

api.add_namespace(ns1)
