# null decorator
def null_decorator(func):
    print('null_decorator')
    return func


@null_decorator
def foo():
    print('bar')


foo()

# args_audit decorator

