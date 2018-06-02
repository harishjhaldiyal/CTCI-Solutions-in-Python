"""
in this problem we just create one empty string and we iterate through the given input string and we copy character by character 
in the new empty string and whenever we see a space and then we copy "%20" instead of copying a space and we iterate through the 
input string only true length number of times which is also given

"""


def func(s,l):
    ns = ""
    for i in range(l):
        if s[i] == ' ':
            ns+="%20"
        else:
            ns+=s[i]
    return ns
