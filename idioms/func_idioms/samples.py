def foo() -> str:
    ''' simple function '''
    return 'bar'


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
def error_msg_format(msg: dict) -> str:
    '''
    format error message
    input: {
        'text': 'service unavailable',
        'code': 1,
        'time': '22:04:51',
        'error_type': 'error',
        }
    output: '22:04:51 - ERROR - 1 - service unavailable'
    '''
    res = ''
    res += msg['time']
    res += ' - ERROR - '
    res += str(msg['code']) + ' - '
    res += msg['text']

    return res


def warning_msg_format(msg: dict) -> str:
    '''
    format warning message
    input: {
        'text': 'too many requests',
        'code': 2,
        'time': '22:09:13',
        'error_type': 'warning',
    }
    output: '22:09:13 - WARNING - 1 - too many requests'
    '''
    res = ''
    res += msg['time']
    res += ' - WARNING - '
    res += str(msg['code']) + ' - '
    res += msg['text']
    return res


def other_msg_format(msg: dict) -> str:
    '''
    format other message
    input: {
        'text':
        'connected',
        'code': 42,
        'time': '22:01:05',
        'error_type': 'other',
        }
    output: '22:01:05 - OTHER - 42 - connected'
    '''
    res = ''
    res += msg['time']
    res += ' - OTHER - '
    res += str(msg['code']) + ' - '
    res += msg['text']
    return res


def msg_format(data: list) -> list:
    ''' format data by error_type'''
    total = []
    msg_type_choices = {
            'error': error_msg_format,
            'warning': warning_msg_format,
            'other': other_msg_format,
            }
    for msg in data:
        if 'error_type' not in msg:
            msg['error_type'] = 'other'

        if msg['error_type'] in msg_type_choices.keys():
            msg_text = msg_type_choices[msg['error_type']](msg)
        else:
            msg_text = msg_type_choices['other'](msg)
        total.append(msg_text)
    return total


error_data = [
    {
        'text': 'service unavailable',
        'code': 1,
        'time': '22:04:51',
        'error_type': 'error',
        },
    {
        'text': 'too many requests',
        'code': 2,
        'time': '22:09:13',
        'error_type': 'warning',
        },
    {
        'text': 'connected',
        'code': 42,
        'time': '22:01:05',
        'error_type': 'other',
        },
    {
        'text': 'monitor is up',
        'code': 666,
        'time': '23:54:18',
        },
    ]


# автовыбор поведения в зависимости от типа события
print('\n'.join(msg_format(error_data)))

# dict choice
tst_msg = {
        'text': 'Dict choice',
        'code': 1,
        'time': '22:04:51',
        'error_type': 'error',
        }

msg_type_choices_tst = {
        'error': error_msg_format,
        'warning': warning_msg_format,
        'other': other_msg_format,
        }

print(msg_type_choices_tst[tst_msg['error_type']](tst_msg))

# list choice

tst_msg1 = {
        'text': 'List choice',
        'code': 1,
        'time': '22:04:51',
        'error_type': 'error',
        }

msg_type_choices_tst1 = [
        error_msg_format,
        warning_msg_format,
        other_msg_format,
        ]

print(msg_type_choices_tst1[0](tst_msg1))

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
