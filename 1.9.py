"""
If we imagine that s2 is a rotation of s1, then we can ask what the rotation point is. For example, if you
rotate waterbottle after wat. you get erbottlewat. In a rotation, we cut s1 into two parts, x and y,
and rearrange them to get s2.
s1 = xy = waterbottle
x = wat
y = erbottle
s2 = yx = erbottlewat
So, we need to check if there's a way to split s1 into x and y such that xy = s1 and yx = s2. Regardless of
where the division between x and y is, we can see that yx will always be a substring of xyxy.That is, s2 will
always be a substring of s1s1.
And this is precisely how we solve the problem: simply do isSubstring(slsl, s2). 
"""


def StringRotation(s1, s2):
    if (check_input(s1, s2)):
        return doubling(s1, s2)
    else:
        return False
        
def check_input(s1, s2):
    if ((len(s1) == len(s2)) and len(s1) > 0):
        return True
    else:
        return False
        
def doubling(s1, s2):
    cs = s1 + s1 #concatenated string
    return process(cs, s2)
    
def process(cs, s2):
    return isSubstring(cs, s2)