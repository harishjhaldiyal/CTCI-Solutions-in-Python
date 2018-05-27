"""
 so the main idea of doing the solution is that we can create an empty hash table in which there will be key value pairs and 
 keys will be the characters in the string and the values will be the number of times a character occurs in the string. 
 MC is a variable which is main counter. MC is initialised to zero in the beginning and the value of MC is incremented by one whenever 
 we iterate through the string and we find a character whose value in the hash table is odd and we decrement the value of MC by one 
 whenever we find the character whose value in the hashtable is even; and the whole idea of doing this problem is that for odd length 
 input string there should be only one character which will occur odd number of times and all the other characters will occur even 
 number of times; and for the even length input string all the characters will occur even number of times and therefore the only 
 legitimate values of MC variable would be zero or one; other than that our input string will not be a permutation of a palindrome.
 
 the above is the best way of doing the problem. the other way is that you can assume that the given string is an ASCII string and based upon 
 that you can create one list having the length 128 and all the values as zero and you increment the value by 1 whenever you see a character 
 in the string based upon the ASCII value of the character and then in the end you check this newly created list again whether all the values 
 are even or not if the given input string is of even length; but if the given input string is odd length then in this newly created list you 
 can check at the end whether all the values are even except for one value which should be odd - if there are more than one values which are 
 all then we can just return false.
 
 """

def func2(s):
    h = {}
    MC = 0 #MC = mainCounter
    for e in s:
        h[e] = 0
    for e in s:
        h[e]+=1
        if (h[e]%2==0):
            MC-=1
        else:
            MC+=1
    if ((MC == 0) or (MC ==1)):
        return True
    else:
        return False
        
def func(s):
    return func2(s)