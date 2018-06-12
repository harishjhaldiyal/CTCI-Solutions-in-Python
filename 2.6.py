"""Solution 1"""


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
        
        
        
"""Solution 2"""

"""
We want to detect linked lists where the front half of the list is the reverse of the second half. How would we
do that? By reversing the front half of the list. A stack can accomplish this.
We need to push the first half of the elements onto a stack. We can do this in two different ways, depending
on whether or not we know the size of the linked list.
If we know the size of the linked list, we can iterate through the first half of the elements in a standard for
loop, pushing each element onto a stack. We must be careful, of course, to handle the case where the length
of the linked list is odd.
If we don't know the size of the linked list, we can iterate through the linked list, using the fast runner/ slow
runner technique described in the beginning of the chapter. At each step in the loop, we push the data from
the slow runner onto a stack. When the fast runner hits the end of the list, the slow runner will have reached
the middle of the linked list. By this point, the stack will have all the elements from the front of the linked
list, but in reverse order. 
"""


#1->2->2->1
#1->2->3->2->1

#[2,1]


"""
both slowptr and fastptr starts from the same place
if fastptr exists and fastptr.next is null -> length of the LL is odd and ignore the middle node
if fastptr exists and fastptr.next is not null -> keep on incrementing slowptr and fastptr
if fastptr doesn't exists -> length of the LL is even
"""

#palindrome2(head)
#process2(head)


def process2(head):
    slowptr = head
    fastptr = head
    stack = []
    while (fastptr is not None):
        if ((fastptr is not None) and (fastptr.next is not None)):
            stack.insert(0,slowptr.value)
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        elif ((fastptr is not None) and (fastptr.next is None)):
            slowptr = slowptr.next
            break
        elif (fastptr is None):
            break
    i = 0
    while (i < len(stack)):
        if (stack[i] != slowptr.value):
            return False
        else:
            i+=1
            slowptr = slowptr.next
    return True
    
    
def palindrome2(head):
    if (input_check(head)):
        result = process2(head)
        if (result):
            print("List is palindrome")
        else:
            print("List is not a palindrome")
    else:
        print("Invalid Input")
        