from flask import Blueprint, request, jsonify
from flask_restplus import Resource, Api, Namespace
from services import pwdgen, get_config
from flask_restplus import reqparse

api = Namespace('pwdgen', description='Create password by default settings')
conf = get_config.get_conf('pwdgen.yml')


@api.route('/')
class GenPassword(Resource):
    def get(self):
        '''
        Generate password by default params
        '''
        pwd_gen = pwdgen.Password()
        pwd = pwd_gen.gen_pwd(conf)
        return {'pwd': pwd}

    @api.param('pwd_length', 'int: password length')
    @api.param('syllables_ratio', 'float: ratio syllables and single charters.\nDefault: ' + str(conf['syllables_ratio']))
    # use single
    @api.param('use_single_nums', 'bool: True or False.\nDefault: ' + str(conf['use_single_nums']))
    @api.param('use_single_letters', 'bool: True or False.\nDefault: ' + str(conf['use_single_letters']))
    @api.param('use_single_symbols', 'bool: True or False.\nDefault: ' + str(conf['use_single_symbols']))
    # use syllable
    @api.param('use_syllable_lowcase_vowels', 'bool: True or False.\nDefault: ' + str(conf['use_syllable_lowcase_vowels']))
    @api.param('use_syllable_upcase_vowels', 'bool: True or False.\nDefault: ' + str(conf['use_syllable_upcase_vowels']))
    @api.param('use_syllable_lowcase_consonants', 'bool: True or False.\nDefault: ' + str(conf['use_syllable_lowcase_consonants']))
    @api.param('use_syllable_upcase_consonants', 'bool: True or False.\nDefault: ' + str(conf['use_syllable_upcase_consonants']))
    # single
    @api.param('single_nums',  'numbers will use to generate password.\nDefault: ' + str(conf['single_nums']))
    @api.param('single_letters',  'letters will be used to generate single characters in password.\nDefault: ' + str(conf['single_letters']))
    @api.param('single_symbols',  'symbols will be used to generate single characters in password.\nDefault: ' + str(conf['single_symbols']))
    # syllable
    @api.param('upcase_syllable_vowels',  'upcase vowels will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_upcase_vowels']))
    @api.param('lowcase_syllable_vowels', 'lowcase vowels will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_lowcase_vowels']))
    @api.param('upcase_syllable_consonants',  'upcase consonants will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_upcase_consonants']))
    @api.param('lowcase_syllable_consonants',  'lowcase consonants will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_lowcase_consonants']))
    def post(self):
        '''Generate password by custom params'''
        parser = reqparse.RequestParser()
        # params
        parser.add_argument(
            'pwd_length',
            type=int,
            default = conf['pwd_length'],
            help='int: password length.\nDefault: ' + str(conf['pwd_length'])
                )
        parser.add_argument(
            'syllables_ratio',
            type=float,
            default = conf['syllables_ratio'],
            help='float: ratio syllables and single charters.\nDefault: ' + str(conf['syllables_ratio'])
                )
        # use single
        parser.add_argument(
            'use_single_nums',
            type=bool,
            default = conf['use_single_nums'],
            help='bool: True or False.\nDefault: ' + str(conf['use_single_nums'])
                )
        parser.add_argument(
            'use_single_letters',
            type=bool,
            default = conf['use_single_letters'],
            help='bool: True or False.\nDefault: ' + str(conf['use_single_letters'])
                )
        parser.add_argument(
            'use_single_symbols',
            type=bool,
            default = conf['use_single_symbols'],
            help='bool: True or False.\nDefault: ' + str(conf['use_single_symbols'])
                )
        # use syllable
        parser.add_argument(
            'use_syllable_lowcase_vowels',
            type=bool,
            default = conf['use_syllable_lowcase_vowels'],
            help='bool: True or False.\nDefault: ' + str(conf['use_syllable_lowcase_vowels'])
                )
        parser.add_argument(
            'use_syllable_upcase_vowels',
            type=bool,
            default = conf['use_syllable_upcase_vowels'],
            help='bool: True or False.\nDefault: ' + str(conf['use_syllable_upcase_vowels'])
            )
        parser.add_argument(
            'use_syllable_lowcase_consonants',
            type=bool,
            default = conf['use_syllable_lowcase_consonants'],
            help='bool: True or False.\nDefault: ' + str(conf['use_syllable_lowcase_consonants'])
            )
        parser.add_argument(
            'use_syllable_upcase_consonants',
            type=bool,
            default = conf['use_syllable_upcase_consonants'],
            help='bool: True or False.\nDefault: ' + str(conf['use_syllable_upcase_consonants'])
            )
        # single
        parser.add_argument(
            'single_nums',
            type=str,
            default = conf['single_nums'],
            help='str: numbers will use to generate password.\nDefault: ' + str(conf['single_nums'])
            )
        parser.add_argument(
            'single_letters',
            type=str,
            default = conf['single_letters'],
            help='str: letters will be used to generate single characters in password.\nDefault: ' + str(conf['single_letters'])
            )
        parser.add_argument(
            'single_symbols',
            type=str,
            default = conf['single_symbols'],
            help='str: symbols will be used to generate single characters in password.\nDefault: ' + str(conf['single_symbols'])
            )
        # syllable
        parser.add_argument(
            'syllable_upcase_vowels',
            type=str,
            default = conf['syllable_upcase_vowels'],
            help='str: upcase vowels will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_upcase_vowels'])
            )
        parser.add_argument(
            'syllable_lowcase_vowels',
            type=str,
            default = conf['syllable_lowcase_vowels'],
            help='str: lowcase vowels will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_lowcase_vowels'])
            )
        parser.add_argument(
            'syllable_upcase_consonants',
            type=str,
            default = conf['syllable_upcase_consonants'],
            help='str: upcase consonants will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_upcase_consonants'])
            )
        parser.add_argument(
            'syllable_lowcase_consonants',
            type=str,
            default = conf['syllable_lowcase_consonants'],
            help='str: lowcase consonants will be used to generate single characters in password.\nDefault: ' + str(conf['syllable_lowcase_consonants'])
            )

        args = parser.parse_args()
        print(args)
        for arg, arg_val in args.items():
            conf[arg] = arg_val
        pwd_gen = pwdgen.Password()
        pwd = pwd_gen.gen_pwd(conf)
        return {'pwd': pwd}

