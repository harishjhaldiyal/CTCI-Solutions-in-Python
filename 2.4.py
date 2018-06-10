"""
 Rather than shifting and swapping elements, we can
actually create two different linked lists: one for elements less than x, and one for elements greater than or
equal to x.
We iterate through the linked list, inserting elements into our before list or our after list. Once we reach
the end of the linked list and have completed this splitting, we merge the two lists. 
"""

def check_input(head):
    if (head is not None):
        return True
    else:
        return False
        
def process(head, par):
    cur_node = head
    small_LL = LinkedList()
    large_LL = LinkedList()
    while (cur_node is not None):
        if (cur_node.value < par):
            small_LL.add(cur_node.value)
        else:
            large_LL.add(cur_node.value)
        cur_node = cur_node.next
        
    cur_node = small_LL.head
    while (cur_node.next is not None):
        cur_node = cur_node.next
    small_LL_tail = cur_node
    small_LL_tail.next = large_LL.head
    return small_LL.head
    
def partition(head, par):
    if (check_input(head)):
        process(head, par)
    else:
        print("Invalid Input")
        
        
"""
In this approach, we start a "resultLL" list. Elements bigger than the pivot element are
put at the tail and elements smaller are put at the head. Each time we insert an element, we update either
the head or tail. 
"""

"""
in this solution you can first of all just write the process2 function and while writing it just mention to the interviewer that you will write the 
addToTail method of linked list class and addToHead method of linked list class later on if the time permits. so first of all you can just complete the 
logic of process2 function and if you have time you can just write addToTail method of linked list class and addToHead method of linked list class.

Similarly, you can do the same thing for check_input function above and all the non-logic-contained functions.
"""

def process2(head,par):
    resultLL = LinkedList()
    cur_noe = head
    while (cur_node is not None):
        if (resultLL.head is None):
            resultLL.addToTail(cur_node.value)
        else:
            if (cur_node.value < par):
                resultLL.addToHead(cur_node.value)
            else:
                resultLL.addToTail(cur_node.value)
        cur_node = cur_node.next
        
def addToTail(self, value):
    node = Node(value)
    if (self.head is None):
        self.head = node
    else:
        cur_node = self.head
        while (cur_node.next is not None):
            cur_node = cur_node.next
        tail_node = cur_node
        tail_node.next = node
        tail_node = node
        
def addToHead(self, value):
    node = Node(value)
    node.next = self.head
    self.head = node
    
    
"""
instead of creating a new linked list for storing our result we can actually rearrange the elements inside the original linked list. 
we do this by iterating the linked list and if we find an element which is less than the partition value then we create a new node of that element and 
we add that node before the head of the original linked list and then we remove that current element and if we find an element whose value is more than 
the partition value or equal to the partition value then we create a new node of that element and we add that new node at the end of the tail of the 
linked list and remove the current element
"""

"""
there are some functions that I have used such as findTail function and lengthLinkedList function. you can mention to the interviewer that you will 
write these functions at the end if you will get time. these functions are understood and you should first right all the logic of the program and 
then write these small functions if the time permits you
"""


def process3(head, par):
    tail = findTail(head)
    prev_node = None
    cur_node = head
    lengthLL = lengthLinkedList(head)
    position = 1
    while (position<=lengthLL):
        if (cur_node == head):
            if (cur_node.value < par):
                prev_node = cur_node
                cur_node = cur_node.next
                position+=1
            else:
                node = Node(cur_node.value)
                tail.next = node
                tail = node
                head = cur_node.next
                cur_node = cur_node.next
                position+=1
        else:
            if (cur_node.value<par):
                prev_node = cur_node
                cur_node = cur_node.next
                position+=1
            else:
                node = Node(cur_node.value)
                tail.next = node
                tail = node
                prev_node.next = cur_node.next
                cur_node = cur_node.next
                position+=1
    return head
            
    