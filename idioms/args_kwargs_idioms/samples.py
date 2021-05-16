def foo(req1: str,  *args, req2: str = 'req2', **kwargs) -> None:
    print('req1', req1)
    print('req2', req2)
    print('args', str(args))
    print('kwargs', str(kwargs))


foo('req1', 1, 2, 3, a='a')
