from flask import request
from flask_restplus import Resource, Namespace, fields
from services import pwdgen_srv, get_config

conf = get_config.get_conf('pwdgen.yml')

pwdgen_ns = Namespace(
        'pwdgen',
        description='Create password by default and custom settings'
        )
pwdgen_list_ns = Namespace(
        'pwdgen_list',
        description='Create list of passwords by default and custom settings'
        )


pwdgen = pwdgen_ns.model('pwdgen', {
    'pwd_length':
        fields.Integer(
            description='int: password length',
            example=conf['pwd_length']
            ),

    'syllables_ratio':
        fields.Float(
            description='float: ratio syllables and single charters.',
            example=conf['syllables_ratio']
            ),

    'use_single_nums':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_single_nums']
            ),

    'use_single_letters':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_single_letters']
            ),

    'use_single_symbols':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_single_symbols']
            ),

    'use_syllable_lowcase_vowels':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_syllable_lowcase_vowels']
            ),

    'use_syllable_upcase_vowels':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_syllable_upcase_vowels']
            ),

    'use_syllable_lowcase_consonants':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_syllable_lowcase_consonants']
            ),

    'use_syllable_upcase_consonants':
        fields.Boolean(
            description='bool: True or False.',
            example=conf['use_syllable_upcase_consonants']
            ),

    'single_nums':
        fields.String(
            description='numbers will use to generate password.',
            example=conf['single_nums']
            ),

    'single_letters':
        fields.String(
            description='letters will be used to \
            generate single characters in password.',
            example=conf['single_letters']
            ),

    'single_symbols':
        fields.String(
            description='symbols will be used to generate \
                    single characters in password.',
            example=conf['single_symbols']
            ),

    'upcase_syllable_vowels':
        fields.String(
            description='upcase vowels will be used to generate \
                    single characters in password.',
            example=conf['syllable_upcase_vowels']
            ),

    'lowcase_syllable_vowels':
        fields.String(
            description='lowcase vowels will be used to generate \
                    single characters in password.',
            example=conf['syllable_lowcase_vowels']
            ),

    'upcase_syllable_consonants':
        fields.String(
            description='upcase consonants will be used to generate \
                    single characters in password.',
            example=conf['syllable_upcase_consonants']
            ),

    'lowcase_syllable_consonants':
        fields.String(
            description='lowcase consonants will be used to generate \
                    single characters in password.',
            example=conf['syllable_lowcase_consonants']
            ),

    }
        )


class GenPassword(Resource):
    def get(self):
        '''
        Generate password by default params
        '''
        pwd_gen = pwdgen_srv.Password()
        res_pwd = pwd_gen.gen_pwd(conf)
        return {'pwd': res_pwd}

    @pwdgen_ns.expect(pwdgen)
    def post(self):
        '''Generate password by custom params'''
        local_conf = conf
        for arg, arg_val in request.json.items():
            local_conf[arg] = arg_val
        pwd_gen = pwdgen_srv.Password()
        res_pwd = pwd_gen.gen_pwd(local_conf)
        return {'pwd': res_pwd}


class GenListPassword(Resource):
    def get(self, pwd_count=conf['def_pwd_count']):
        '''
        Generate list passwords by default params
        '''
        if pwd_count > conf['max_pwd_count']:
            return {'error': f'max pwd_count is {conf["max_pwd_count"]}'}
        res_pwd_list = []
        pwd_gen = pwdgen_srv.Password()
        for _ in range(int(pwd_count)):
            res_pwd_list.append(pwd_gen.gen_pwd(conf))
            print(pwd_gen.gen_pwd(conf))
        return {'pwd_list': res_pwd_list}

    @pwdgen_ns.expect(pwdgen)
    def post(self, pwd_count):
        '''Generate list passwords by custom params'''
        local_conf = conf
        res_pwd_list = []
        for arg, arg_val in request.json.items():
            local_conf[arg] = arg_val
        pwd_gen = pwdgen_srv.Password()
        pwd = pwd_gen.gen_pwd(local_conf)
        for _ in range(int(pwd_count)):
            res_pwd_list.append(pwd_gen.gen_pwd(local_conf))
        return {'pwd_list': res_pwd_list}
