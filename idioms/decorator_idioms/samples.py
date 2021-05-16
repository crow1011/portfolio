# null decorator
def null_decorator(func):
    print('null_decorator')
    return func


@null_decorator
def foo():
    print('bar')


foo()

# args_audit decorator

def trace_decorator(func):
    ''' print args, kwargs and func result '''
    def wrapper(*args, **kwargs):
        print(f'_-_- start trace {func.__name__}() _-_-')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        print(f'RUN {func.__name__}(*args, **kwargs)')
        original_res = func(*args, **kwargs)
        print(f'func RETURN: {original_res}')
        print(f'_-_- end trace {func.__name__}() _-_-')
        return original_res
    return wrapper

@trace_decorator
def spam(a, b):
    return a+b

spam(1,b=2)
