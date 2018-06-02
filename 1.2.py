"""
in method one first of all we check whether the length of both input strings are equal or not, if not then we will just 
return false directly. next we throw one of the strings in a hash table - the keys will be the ASCII value of the characters 
in the string and the value will be the characters of that ASCII value and then in the other string we iterate through the 
characters we calculate the ASCII value of every character and then in the hashtable we search whether that character exists 
or not, if it exists then we just remove it from the hash table because this will deal with the duplicate characters, but if 
we cannot find that character in the ASCII value or if we cannot find the ASCII value in the hash table then it will 
automatically return false. and in method 2 we will assume that the given string is ASCII string, we will create one 
list of 128 length having all the elements 0 and then we iterate through the first string, we calculate the ASCII value 
and in that index we will increment value by 1 and then we iterate through the second string we calculate the ASCII value 
of every character and then at that index in the list we will be decrement the value by 1 and if any of the value in the 
list is less than 0 then we will automatically return false which means that there is additional character in the second 
string and then at the end we check whether all the values in the list are 0 or not - we can do this by two ways: the one 
way will be just to calculate the sum because the sum of all the values should be 0; the other ways that we check one by 
one if any of the element is not zero then return false

"""


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
        
