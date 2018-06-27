"""
array = [ 2,3,4,5,6,7,8,9,10 ]

n elements; n nodes
Time complexity: O ( n )
Space complexity: O ( n )
"""


def MinimalBST ( input ):

	if ( input_check ( input ) ):
		BST ( input, 0, len ( input ) - 1 )
	
	else:
		print ( "Invalid Input" )
		return


def BST ( input, start, end ):

	if ( start > end ):
		return

	else:
                middleIndex = int ( ( start + end ) / 2 )
                treenode = TreeNode ( input [ middleIndex ] )
                treenode.left = BST ( input, start, middleIndex - 1 )
                treenode.right = BST ( input, middleIndex + 1, end )
                return treenode


	
"""
Test Cases:

input = [ 2,3,4,5,6,7,8,9,10 ]

"""



