"""

1. Run through each linked list to get the lengths and the tails.
2. Compare the tails. If they are different (by reference, not by value), return immediately. There is no inter
section.
3. Set two pointers to the start of each linked list.
4. On the longer linked list, advance its pointer by the difference in lengths.
5. Now, traverse on each linked list until the pointers are the same

"""

"""functions:

1. intersection (headA, headB)

2. input_check (headA, headB)

3. process (headA, headB)

4. getLengthAndTail (head)

5. one class called "lengthAndTail" to bound length and tail and the return from a function"""

"""
1->2->3->4->x

   5->6->



"""


def process (headA, headB):
    resultA = getLengthAndTail (headA) #you are not taking any risk because you are passing by reference, not by value, and also the return is a reference
    resultB = getLengthAndTail (headB)
    
    if (resultA.tail != resultB.tail):
        print ("No intersection")
    
    else:
        # DO NOT swap the head nodes in the following manner because then only the head nodes would be swapped and not the other nodes
        """if (resultA.length > resultB.length):
            headA, headB = headB, headA"""
            
        biggerList = headA if (resultA.length >= resultB.length) else headB
        shorterList = headA if (resultA.length < resultB.length) else headB
               
        ptr1 = getKthNode (biggerList, resultA.length, resultB.length) #you are not taking any risk because you are passing by reference, not by value, and also the return is a reference
        ptr2 = shorterList
        while (ptr1 != ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
        
def input_check(headA, headB):
    if ((headA is None) or (headB is None)):
        return False
    else:
        return True
        
def intersection (headA, headB):
    if (input_check (headA, headB)):
        reference = process (headA, headB)
        return reference
        
    else:
        print ("Invalid Input")
        
def getKthNode (headA, lenA, lenB):
    diff = abs(lenA - lenB)
    ptr1 = headA
    for i in range (1,diff+1):
        ptr1 = ptr1.next
    return ptr1
        
def getLengthAndTail (head):
    tail = None
    length = 0
    ptr = head
    while (ptr is not None):
        length += 1
        if (ptr.next is None):
            tail = ptr
        ptr = ptr.next
        
    result = lengthAndTail (length, tail)
    return result
    
        
        
class lengthAndTail (object):
    def __init__(self, length, tail):
        self.length = length
        self.tail = tail
        
    def length (self):
        return self.length
        
    def tail (self):
        return self.tail
        
    