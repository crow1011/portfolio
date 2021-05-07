import time


error_message = 'EGOR!!!!!1!'
error_code = 42

# string formatting option 1: percent character
tst1 = '1.1. %s - %s - 0x%x' % (time.time(), error_message, error_code)
print(tst1)

tst2_data = {
        'message': error_message,
        'code': error_code,
        'time': time.time(),
        }
tst2 = '1.2. %(time)s - %(message)s - 0x%(code)x' % tst2_data
print(tst2)

# string format option 2: via call .format()
tst3_data = (
        time.time(),
        error_message,
        error_code,
        )
tst3 = '2.1. {} - {} - {:#x}'.format(*tst3_data)
print(tst3)

tst4 = '2.2. {time} - {message} - {code:#x}'.format(
        time=time.time(),
        message=error_message,
        code=error_code,
        )
print(tst4)

# string format option 3: via f-string

tst5 = f'3.1. {time.time()} - {error_message} - {error_code:#x}'
print(tst5)

# string format option 4: with string.Template

from string import Template
t = Template('4.1. $time - $message - $code')
tst6 = t.substitute(
        time=time.time(),
        message=error_message,
        code=hex(error_code),
        )
print(tst6)
