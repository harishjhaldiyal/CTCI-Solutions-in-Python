"""
first of all we can check the length of both input strings, 
which means that for insertion or removal case the length of 
the one string should be only one more or one less than the other 
string; but for the replacement case the length of the strings 
should be equal. Other than these two cases we can straight away return false. 
Now, we can start checking by putting the flag as false in the beginning and then 
for insertion or removal case we can assign the bigger length string to s1 and smaller length string to s2; 
and for replacement case it doesn't matter which one is S1 or S2. Then we adopt a 2 pointer approach in which 
the first pointer will point to the 1st string and the second pointer will point to the second string and as soon as we will find that the 
character at which the first pointer is pointing to is not equal to the character at which the second pointer is pointing to and if the flag 
is already true then we can straight away return false which means that we have already seen one case like this in the past and we cannot ignore 
it second time; otherwise we can flip the value of flag to be true because this is the first time that we are seeing this case and if it is the 
case of insertion or removal of character than we  increment the pointer of the biggest string by one; in the case of replacement we increment the 
pointer of both the strings by one and at the end we will check that if the flag is true which means that the strings are one edit away then we can 
return true otherwise we can return false
"""

def l(s1,s2):
    if ((len(s1) == len(s2)) or (len(s1) == 1+len(s2))):
        return func(s1,s2)
        """
        please note that the difference between calling a function without 'return' keyword and calling a function with 'return' 
        keyword is that if you call a function without 'return' keyword then after implementing that function the process will come 
        back to this function from where the function was called; but if you will call a function with 'return' keyword then after 
        implementing that function the process will not come back to the original function because you have already returned the value 
        from it and the function cannot return more than once
        """
    elif (len(s2) == 1+len(s1)):
        return func(s2,s1)  
    else:
        return False
        
        
def func(s1,s2):
    flag = False
    i,j = 0,0
    while (i<len(s1) and j<len(s2)):
        if (s1[i]!=s2[j]):
            if (flag):
                return False
            else:
                flag = True
                i+=1
                if (len(s1) == len(s2)):
                    j+=1
        else:
            i+=1
            j+=1
    if (i<len(s1)): #for cases like s1 = "abcd" and s2 = "abc"
        return True
    if (flag):
        return True
    else:
        return False
        
        
def f(s1,s2):
    return l(s1,s2)