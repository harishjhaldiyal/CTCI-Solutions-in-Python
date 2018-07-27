"""
						6

					5			7
				
				9		0	1		2

nodeA = 7
nodeB = 2


smaller example:

					8

						0
						
							9

nodeA = 9
nodeB = 0


special case:

					8

				6


Pseudocode:

1) if root.left exists, search on the left subtree of the root whether both nodes (a), or either node (b), or no node exist (c)

2) otherwise update the root node to root.right and repeat step 1

a) update root node to the left child of the actual root node and repeat step 1

b) return root node

c) update root node to the right child of the actual root node and repeat step 1

3) if root node is nodeA or nodeB, then return root node

time complexity: O (n) -> n is the number of nodes
space complexity: O (n)
"""

# code:

def lowestCA ( nodeA, nodeB, root ):

	if ( root == nodeA or root == nodeB ):
		return root.value

	if ( root.left is not None ):

		foundNodeA = search ( root.left, nodeA )
		foundNodeB = search ( root.left, nodeB )

		if ( foundNodeA and foundNodeB ):
			root = root.left
			return lowestCA ( nodeA, nodeB, root )

		if ( ( foundNodeA and not foundNodeB ) or ( foundNodeB and not foundNodeA )):
			return root.value


	root = root.right
	return lowestCA ( nodeA, nodeB, root )




def userInterface ( nodeA, nodeB, root ):

	if ( input_check ( nodeA, nodeB, root ) ):
		return lowestCA ( nodeA, nodeB, root )

	else:
		print ( "Invalid Input" )
		return
