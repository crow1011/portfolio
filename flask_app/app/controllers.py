from flask import Blueprint, request, jsonify
from .utils import info



mod_tst = Blueprint('tst', __name__, url_prefix='/tst')
mod_gen = Blueprint('gen', __name__, url_prefix='/gen')


@mod_tst.route('/', methods=['POST', 'GET'])
def tst():
    return 'OK'


@mod_gen.route('', methods=['POST', 'GET'])
def gen():
    if request.method == 'GET':
        return jsonify(info('invalid_nethod'))
    print(request.json)
    return 'nice'
