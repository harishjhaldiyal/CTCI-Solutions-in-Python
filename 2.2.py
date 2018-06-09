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
the whole idea of doing this solution is that we are finding the index of the current node and the index is starting from the end of the linked list 
which means that if there are n nodes in the linked list then the index of the first node would be n and the index with of the last note would be 1; 
therefore we are performing a recursive solution and when we get the index of the current node, we also check that if the index is equal to K - if it 
is equal to k then we are sure that the current node is the K-th to the last node and we return the value for that node
"""


def recursiveSolution(head, k):
    if (head is None):
        return 0
    index = recursiveSolution(head.next,k)+1
    if(index == k):
        print(str(k)+"th to last node is "+str(head.val))
    return index