class A(object):
    def __init__(self, st):
        self.s = st
        self.L = [False]*128
    def UniqueChars(self):
        for i in self.s:
            val = ord(i)
            if self.L[val]:
                return False
            else:
                self.L[val] = True
        return True