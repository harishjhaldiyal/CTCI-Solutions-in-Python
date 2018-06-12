"""palindrome(head)
input_check(head)
reverse(head)
process(head1, head2)"""

#1->2->1->x
#1->x

"""
 We know that,
since it's a palindrome, the list must be the same backwards and forwards. This leads us to our first solution.
Our first solution is to reverse the linked list and compare the reversed list to the original list. If they're the
same, the lists are identical. 
"""

def input_check(head):
    if (head is not None):
        return True
    else:
        return False
        
def reverse(head): # input: 1->2->1->x #reversed list: 1->2->1->x
    headRev = None
    ptr = head
    while (ptr is not None):
        data = ptr.value
        nodeRev = Node(data)
        nodeRev.next = headRev
        headRev = nodeRev
        ptr = ptr.next
    return headRev
    
def process(head1, head2): #head2 - > reversed linked list; head1-> input linked list #input: 1->2->1->x #reversed list: 1->2->1->x
    ptr1 = head1
    ptr2 = head2
    while ((ptr1 is not None) and (ptr2 is not None)):
        if (ptr1.value != ptr2.value):
            return False
        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
    return True
    
def palindrome(head):
    if (input_check(head)):
        headRev = reverse(head)
        result = process(head, headRev)
        if (result):
            print("List is palindrome")
        else:
            print("List is not a palindrome")
    else:
        print("Invalid Input")