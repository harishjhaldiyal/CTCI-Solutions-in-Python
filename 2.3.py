"""
The solution is simply to copy the data from the next node over to the current node, and then to delete the
next node. 
one very important point to note is that you cannot just put another note into the current note simply by n = n.next. you have to copy the value in the 
next node to the current node and the pointer of the next node to the current node to be able to clone the next note to the current node. another important 
point to note is that in this solution you cannot remove the last node in the linked list because node.next.value will throw an error because node.next.value 
doesn't exist. node.next is not any instance of a class so if node.next is not an instance of a class then node.next.value will obviously be not any entity 
therefore it will throw an error
"""


def deleteMiddleNode(node):
    if ((node is None) or (node.next is None)):
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next