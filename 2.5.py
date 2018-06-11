"""
Iterative Approach
"""

"""
in the iterative solution, we have two linked lists and the length of both the linked list. First we check input and again you can tell your interviewer 
that you will perform the check_input function later on if you will get time and based upon the length you can just assign l1 and l2 and just pass it into 
the process function where you first create an empty linked list and then based upon the iteration starting from the head of both the linked list you just 
calculate the sum and finally returned the whole resultant linked list
"""

def sumLL(LL1, LL2, len1, len2):
    if check_input(LL1,LL2):
        if (len1>=len2):
            l1 = LL1
            l2 = LL2
        else:
            l1 = LL2
            l2 = LL1
        process(l1,l2)
    else:
        print("Invalid Input")
        
def process(l1,l2):
    resultLL = LinkedList()
    carry = 0
    ptr1 = l1.head
    ptr2 = l2.head
    while((ptr1 is not None) or (ptr2 is not None)):
        summ = 0
        if (ptr1 is not None):
            summ += ptr1.value
        if (ptr2 is not None):
            summ += ptr2.value
        summ += carry
        if (summ>9):
            carry = 1
            val = summ%10
            resultLL.add(val)
        else:
            carry = 0
            resultLL.add(summ)
    if (carry == 1):
        resultLL.add(carry)
    return resultLL
    
    
"""
RECURSIVE SOLUTION
"""

"""
in the recursive approach, unlike the iterative approach, in the parameters you do not have the linked list instead you have the head nodes of two linked lists 
and carry and based upon the checking you just calculate the sum and you just keep on returning the calculated node from the functions and then to link all the 
recursive functions you need to connect the nodes of all the functions and that can be connected by resultNode.next equals to the recursive function. carefully 
checked the null point exception errors cases.

In implementing this code, we must be careful to handle the condition when one linked list is shorter than
another. We don't want to get a null pointer exception. 
"""

def process2(node1, node2, carry):
    if ((node1 is not None) or (node2 is not None)):
        summ = 0
        if (node1 is not None):
            summ += node1.val
        if (node2 is not None):
            summ += node2.val
        summ += carry
        if (summ > 9):
            val = summ%10
            carry = 1
            resultNode = Node(val)
        else:
            carry = 0
            resultNode = Node(summ)
        resultNode.next = process2(None if (node1 is None) else node1.next, None if (node2 is None) else node2.next, carry)
    else:
        if (carry ==1):
            resultNode = Node(1)
            return resultNode
        else:
            return
            
            
"""
One list may be shorter than the other, and we cannot handle this "on the flY:' For example, suppose we
were adding (1 -> 2 -> 3-> 4) and (5-> 6-> 7). We need to know that the 5 should be"matched"with the
2, not the 1. We can accomplish this by comparing the lengths of the lists in the beginning and padding
the shorter list with zeros.

We start the iteration from the starting of the linked lists and add the corresponding nodes with taking care of the case when head nodes are added.
"""


def followUpIteratively(l1, l2):
    len1 = lengthLL(l1)
    len2 = lengthLL(l2)
    if (len2 < len1):
        l2 = addPadding(l2, len1 - len2)
    resultLL = LinkedList()
    ptr1 = l1.head
    ptr2 = l2.head
    carry = 0
    while ((ptr1 is not None) and (ptr2 is not None)):
        summ = ptr1.value + ptr2.value
        if (summ > 9):
            twosPos = int(summ/10)
            onesPos = int(summ%10)
            val = twosPos + carry
            resultLL.add(val)
            carry = onesPos
        else:
            if ((ptr1 == l1.head) and (ptr2 == l2.head)):
                carry = summ
            else:
                val = carry
                resultLL.add(val)
                carry = summ
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    resultLL.add(carry)
    return resultLL
        
        
def followUpRecursively(head1, head2, carry, flag):
    """
    ASSUMING THAT THE CODE IN THIS COMMENT HAS ALREADY BEEN CHECKED
    len1 = lengthLL(head1)
    len2 = lengthLL(head2)
    if (len2 < len1):
        head2 = addPadding(head2, len1 - len2)"""
    if ((head1 is None) and (head2 is None)):
        node = Node(carry)
        return node
    else:
        summ = head1.value + head2.value
        if (summ > 9):
            twosPos = int(summ/10)
            onesPos = int(summ%10)
            val = twosPos+carry
            node = Node(val)
            carry = onesPos
            node.next = followUpRecursively(head1.next, head2.next, carry, flag)
            return node
        else:
            if (flag):
                carry = summ
                flag = False
                node = followUpRecursively(head1.next, head2.next, carry, flag)
                return node
            else:
                val = carry
                node = Node(val)
                carry = summ
                node.next = followUpRecursively(head1.next, head2.next, carry, flag)
                return node
        
        