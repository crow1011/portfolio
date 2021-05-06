class UnderlineTst:
    def __init__(self):
        self.foo = 1
        self._bar = 42
        self.__egg = 13
        self.__tst__ = 321

class ChildUnderlineTst(UnderlineTst):
    def __init__(self):
        super().__init__()
        self.__egg = 'children'
        self.__tst__ = 'tst'

_GlobalUnderlineTst__tst = 666
class GlobalUnderlineTst:
    def call_global(self):
        return __tst
