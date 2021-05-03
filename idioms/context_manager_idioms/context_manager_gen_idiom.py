import time
from contextlib import contextmanager


@contextmanager
def context_timer() -> None:
    '''
    simple context manager
    for measuring code execution time
    '''
    try:
        start_time = time.time()
        yield
    finally:
        print('Total: ', time.time() - start_time)


with context_timer() as timer:
    print('# Start')

    print('# Sleep 3s')
    time.sleep(3)

    print('# Print total')
