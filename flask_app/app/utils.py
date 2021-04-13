def info( error='Internal Error') -> dict:
    ''' Gen help info and return error info dict '''
    info = {
        'error': error,
        'info': 'for generate new password send method POST and params',
        'example': ''' curl -XPOST -d '{"type": "default"}' http://localhost:5000/gen'''}
    return info


