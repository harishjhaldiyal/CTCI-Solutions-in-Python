"""
					6

			3				9
	
		2		4		7		10

"""
""" Solution 1: In-Order Traversal Our first thought might be to do an in-order traversal, copy the elements to an array, and then check to see if the array is sorted. This solution takes up a bit of extra memory, but it works-mostly. The only problem is that it can't handle duplicate values in the tree properly. However, if we assume that the tree cannot have duplicate values, then this approach works. """

def inorder ( root, LON ):		# LON -> listOfNodes
	
	if ( root is not None ):
            inorder ( root.left, LON )
            LON.append ( root )
            inorder ( root.right, LON )


def isSorted ( LON ):

	i = 1
	while ( i < len ( LON ) ):
		if ( LON [ i ] >= LON [ i - 1 ] ):
			return False
		i += 1

	return True


def userInterface ( root ):

	if ( input_check ( root ) ):
		LON = [ ]
		inorder ( root, LON )
		return isSorted ( LON )

	else:
		print ( "Invalid Input" )
		return

""" Solution 2: When we examine the above solution, we find that the array is not actually necessary. We never use it other than to compare an element to the previous element. So why not just track the last element we saw and compare it as we go?"""

def inorder ( root, VPTNob ):		# VPTNob -> valueOfPreviouslyTraversedNodeObject
	
	if ( root is None ):
		return True

        if ( not inorder ( root.left, VPTNob ) ):
                return False

        if ( VPTNob.getter ( ) is not None and root.value <= VPTNob.getter ( ) ):
                return False
        VPTNob.setter ( root.value )

        if ( not inorder ( root.right, VPTNob ) ):
                return False

        return True


def userInterface ( root ):

	if ( input_check ( root ) ):
		ob = VPTN ( None )
		return inorder ( ob )
	else:
		print ( "Invalid Input" )
		return


class VPTN ( object ):

	def __init__ ( self, vptn ):
		self.vptn = vptn

	def setter ( self, vptn ):
		self.vptn = vptn

	def getter ( self ):
		return self.vptn

"""
Solution #3: The Min / Max Solution 
In this solution, we leverage the definition of the binary search tree. What does it mean for a tree to be a binary search tree? We know that it must, of course, satisfy the condition left. data <= current. data < right. data for each node, but this isn't quite sufficient. More precisely, the condition is that all left nodes must be less than or equal to the current node, which must be less than all the right nodes. Using this thought, we can approach the problem by passing down the min and max values. As we iterate through the tree, we verify against progressively narrower ranges. 
When we branch left, the max gets updated. When we branch right, the min gets updated. If anything fails these checks, we stop and return false. The time complexity for this solution is O(N), where N is the number of nodes in the tree. We can prove that this is the best we can do, since any algorithm must touch all N nodes. Due to the use of recursion, the space complexity is O ( log N) on a balanced tree. There are up to O ( log N) recursive calls on the stack since we may recurse up to the depth of the tree.
"""

"""
					6

			3				9
	
		2		4		7		10


move to left child -> min remains the same, max changes to current node's value
move to right child -> max remains the same, min changes to current node's value + 1

"""














def isBST ( root, min, max ):

	if ( root is None ):
		return True

        if ( not isBST ( root.left, min, root.value ) ):
                return False

        if ( min is not None ):
                if ( root.value < min ):
                        return False

        if ( max is not None ):
                if ( root.value >= max ):
                        return False

        if ( not isBST ( root.right, root.value + 1, max ) ):
                        return False

        return True


def userInterface ( root ):

	if ( input_check ( root ) ):
		return isBST ( root, None, None )

	else:
		print ( "Invalid Input" )
		return
