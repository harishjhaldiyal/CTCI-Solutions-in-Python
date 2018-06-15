"""For mathematical reason of the following, please refer to page 223 of CTCI

1. Create two pointers, FastPointer and SlowPointer. 
2. Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step. 
3. When they collide, move SlowPointer to LinkedListHead. Keep FastPointer where it is. 
4. Move SlowPointer and FastPointer at a rate of one step. Return the new collision point."""


"""process (head)
input_check (head)
linkedListLoop (head)
existLoop (head)"""

"""
examples:

1 -> 1

1 -> 2 -> 3 -> 4 -> 5 -> 3


"""


def process ( head ):
	flag = False
	slowptr = head
	fastptr = head
	
	while ( True ):
		if ( flag ):
			slowptr = slowptr.next		# 3
			fastptr= fastptr.next		# 3
			if ( slowptr == fastptr ):
				return slowptr

		else:
			slowptr = slowptr.next		# 4
          		fastptr = fastptr.next.next	# 4
          		if ( slowptr == fastptr ):
            			flag = True
            			slowptr = head

def existLoop ( head ):
	
	slowptr = head
	fastptr = head
	
	while ( True ):
		if ( fastptr is None ):
			return False

		if ( fastptr.next is None ):
			return False

		slowptr = slowptr.next		# 4
		fastptr = fastptr.next.next	# 4
		if ( slowptr == fastptr ):
			return True



def input_check ( head ):

	if ( head is not None ):
		return True

	else:
		return False

	

def linkedListLoop ( head ):

	if ( input_check ( head ) and existLoop ( head ) ):
		node = process ( head )
		return node

	else:
		print ("Either the linked list is empty or the loop doesn't exist")
