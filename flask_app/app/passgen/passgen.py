from flask import Blueprint, request, jsonify
from .utils import info


mod_gen = Blueprint('gen', __name__, url_prefix='/gen')

@mod_gen.route('', methods=['POST', 'GET'])
def gen():
    '''
    генерирует пароль с дефолтными или кастомными настройками
    '''
    if request.method == 'GET':
        return jsonify(info('invalid_nethod'))
    print(request.json)
    return 'nice'
