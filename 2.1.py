"""
In order to remove duplicates from a linked list, we need to be able to track duplicates. A simple hash table
will work well here.
In the below solution, we simply iterate through the linked list, adding each element to a hash table. When
we discover a duplicate element, we remove the element and continue iterating. We can do this all in one
pass since we are using a linked list. 
"""

def check_input(L):
    root = L.head
    if (root is not None):
        return True
    else:
        return False
        
def no_dups(L):
    if (check_input):
        hset = set()
        cur_node = L.head
        prev_node = None
        while (cur_node is not None):
            if (cur_node.val in hset):
                prev_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                hset.add(cur_node.val)
                prev_node = cur_node
                cur_node = cur_node.next
        return L
    else:
        print ("Invalid Input")
        
        
"""
lfwe don't have a buffer, we can iterate with two pointers: current which iterates through the linked list,
and runner which checks all subsequent nodes for duplicates. 
"""



def followUp(L):
    if (check_input):
        node = L.head
        cur_node = node
        while (cur_node is not None):
            runner = cur_node.next
            prev_node_runner = cur_node
            while (runner is not None):
                if (cur_node.val == runner.val):
                    prev_node_runner.next = runner.next
                prev_node_runner = runner
                runner = runner.next
            cur_node = cur_node.next
    else:
        print ("Invalid Input")