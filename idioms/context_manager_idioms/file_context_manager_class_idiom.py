class FileContextManager:
    '''
    context manager for safe opening and closing of a file
    '''
    def __init__(self, name, open_mode):
        self.name = name
        self.open_mode = open_mode

    def __enter__(self):
        self.file = open(self.name, self.open_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.file:
            self.file.close()



if __name__=='__main__':
    with FileContextManager('tst.txt', 'w') as f:
       f.write('42')
