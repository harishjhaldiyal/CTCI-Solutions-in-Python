"""
first of all starting from func1(), first we anticipate the length of the compressed string without even calculating the compressed 
string and then we try to figure out if the length of the compressed string is greater than or equal to the length of input string or not. 
if it is greater than or equal to the length of input string, then there is no point of calculating the compressed string - we can directly 
return the input string; otherwise we have to calculate the compressed string which is in func2() and for doing that I am appending all the new 
characters in the list of characters and not a string because appending in the string frequently is very expensive in terms of time but appending 
in a list is a constant time operation and then at the end I am applying the join method of string to convert the list of characters into a string 
and I just return that final compressed string (fcs). there is one more point to take note of that I have a list called CS which means compressed 
string and I cannot directly access cs[-1] if there is nothing in CS - it will throw an error to me so to tackle with this I have to separate create 
case for when 'i' is zero inside the for loop so that there is something inside CS first before executing anything related to cs[-1]

"""


def func1(s):
    lcs = 1
    for i in range(len(s)):
        if i>=1:
            if (s[i]!=s[i-1]):
                lcs+=2
    lcs+=1
    if (lcs>=len(s)):
        return False
    else:
        return True
        
def func2(s):
    if func1(s):
        counter = 0
        cs = []
        for i in range(len(s)):
            if (i==0):
                cs.append(s[i])
                counter+=1
                continue
            if (cs[-1]==s[i]):
                counter+=1
            else:
                cs.append(str(counter))
                cs.append(s[i])
                counter = 1
        cs.append(str(counter))
        fcs = ''.join(cs)
        return fcs
    else:
        return s