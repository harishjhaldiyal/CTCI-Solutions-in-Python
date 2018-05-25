# METHOD 1:

def Pal(s1,s2):
    if (len(s1) != len(s2)):
        return False
    D = {}
    for c in s2:
        val = h(c)
        D[val] = []
        D[val].append(c)
    for i in s1:
        val = h(i)
        if val not in D:
            return False
        if i in D[val]:
            D[val].remove(i)
        else:
            return False
    return True
    
def h(c):
    return ord(c)%64
    
    
# METHOD 2:

def Pal2(s1,s2):
    L = [0]*128
    for i in s1:
        val = ord(i)
        L[val]+=1
    for e in s2:
        val = ord(e)
        L[val]-=1
        if (L[val]<0):
            return False
    if sum(L)==0:
        return True
    else:
        return False
    """for e in L:
        if e!=0:
            return False
    return True"""
        