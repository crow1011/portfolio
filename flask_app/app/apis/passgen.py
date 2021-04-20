from flask import Blueprint, request, jsonify
from flask_restplus import Resource, Api, Namespace
from services import pwdgen, get_config
api = Namespace('default', description='Create password by default settings')


@api.route('/')
class HelloWorld(Resource):
    def get(self):
        '''
        gen pwd by default params
        '''
        conf = get_config.get_conf('pwdgen.yml')
        pwd_gen = pwdgen.Password()
        pwd = pwd_gen.gen_pwd(conf)
        return {'pwd': pwd}


