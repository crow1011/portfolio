import time


class ContextTimer:
    '''
    the context manager prints the elapsed time
    on call and total time on completion
    '''
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self.check_timer

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Total:', time.time() - self.start_time)

    def check_timer(self) -> int:
        return time.time() - self.start_time


if __name__ == '__main__':
    with ContextTimer() as timer:
        print('# Start')

        print('# Sleep 1s')
        time.sleep(1)
        print('# Check timer')
        print(timer())

        print('# Sleep 2s')
        time.sleep(2)
        print('# Check timer')
        print(timer())

        print('# Print total')
