from flask import Blueprint, request

mod_tst = Blueprint('tst', __name__, url_prefix='/tst')


@mod_tst.route('/', methods=['POST', 'GET'])
def tst():
    return 'OK'
