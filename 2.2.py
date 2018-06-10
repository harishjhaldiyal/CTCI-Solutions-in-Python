"""
 the kth to last element is the (length - k+1)th element. We can
just iterate through the linked list to find this element
"""

def input_check(k,l):
    if (k<=l):
        return True
    else:
        return False
        
def LLLength(node):
    l = 0
    if (node is not None):
        cur_node = node
        while (cur_node is not None):
            l+=1
            cur_node = cur_node.next
        return l
        
def returnK(head,k):
    lenLL = LLLength(head)
    if (input_check(k,lenLL)):
        nodeToReturn = lenLL-k+1
        cur_node = head
        position = 1
        while (position<nodeToReturn):
            cur_node = cur_node.next
            position+=1
        return cur_node
    else:
        print("Invalid input")
        return None
    print("Zero length of the linked list")
    return None
    
"""
A more optimal, but less straightforward, solution is to implement this iteratively. We can use two pointers,
slow_node and fast_node. We place them k nodes apart in the linked list by putting slow_node at the beginning and moving fast_node
k nodes into the list. Then, when we move them at the same pace (one at a time) following the logic that first we increase the fast_node by one and then we check
if this new fast_node is not None - if it is not None then we inrease the slow_node by one, otherwise we will return the slow_node which will be the
k-th node from the last
"""


def twoPointer(head,k):
    lenLL = LLLength(head)
    if (input_check(k,lenLL)):
        cur_node = head
        position = 1
        while(position<k):
            cur_node = cur_node.next
            position+=1
        fast_node = cur_node
        slow_node = head
        while (True):
            fast_node = fast_node.next
            if (fast_node is not None):
                slow_node = slow_node.next
            else:
                return slow_node
                
"""
This algorithm recurses through the linked list. When it hits the end, the method passes back a counter set
to 0. Each parent call adds 1 to this counter. When the counter equals k, we know we have reached the kth
to last element of the linked list.
"""


def recursiveSolution(head, k):
    if (head is None):
        return 0
    index = recursiveSolution(head.next,k)+1
    if(index == k):
        print(str(k)+"th to last node is "+str(head.val))
    return index