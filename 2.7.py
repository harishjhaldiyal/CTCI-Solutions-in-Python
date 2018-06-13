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

3. process (headA, headB)"""

"""
1->2->3->4->x

   5->6->



"""


def process (headA, headB):
    tailA = None
    tailB = None
    lenA = 0
    lenB = 0
    ptrA = headA
    ptrB = headB
    while (ptrA is not None):
        lenA += 1
        if (ptrA.next is None):
            tailA = ptrA
        ptrA = ptrA.next
    
    while (ptrB is not None):
        lenB += 1
        if (ptrB.next is None):
            tailB = ptrB
        ptrB = ptrB.next
        
    if (tailA != tailB):
        print ("No intersection")
    
    else:
        if (lenB > lenA):
            headA, headB = headB, headA
        
        ptr1 = headA
        ptr2 = headB
        diff = abs(lenA - lenB)
        while (ptr1 != ptr2):
            for i in range (1,diff+1):
                ptr1 = ptr1.next
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
        
    