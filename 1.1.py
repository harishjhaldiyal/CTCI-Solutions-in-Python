"""
the whole idea of doing this problem is that we can create one list having length 128 and all the elements in the list are 
initialised to false and then we iterate through the string and for every character we calculate it's ASCII value and that 
ASCII value will act as the index in the list and at that index we change the value from false to true and then we continue 
iterating through the string and if there are any duplicate then it must be already true in the list so if it is already true 
then it means that we have already seen that in the past and we can just straight away return false. please note that the Assumption 
is that the given input string is an ASCII string that's why we can create a list of length 128
"""

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
