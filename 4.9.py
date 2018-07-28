"""
BST:

				10

			1			20

		0		2	15		25

array1 = [ 10, 1, 0, 2, 20, 15, 25 ]
array2 = [ 10, 20, 25, 15, 1, 2, 0 ]
array3 = [ 10, 1, 20, 0, 2, 15, 25 ]

array = [ 10, 1, 20, 0, 2, 15, 25 ]

preorder - root, left, right
preorder - root, right, left
level order traversal

Time complexity : O ( n + n + n ) = O ( n )
Space complexity: O ( n + n + n ) = O ( n )




array = [ 1, 2, 3 ]

			1
		
				2

					3




			2
		
		1		3





			3

		2

	1
"""
#code:

def BSTSequences ( root ):

	array1 = preorder1 ( root )
	array2 = preorder2 ( root )
	array3 = levelOrderTraversing ( root )
	array = [ ]
	if ( different ( array1, array2, array3 ) ):
		return addArrays1 ( array1, array2, array3, array )

	elif ( twoArraysSame ( array1, array2, array3 ) ):
		result = twoDifferentArraysHelper ( array1, array2, array3 )
		firstArray = result [ 0 ]
		secondArray = result [ 1 ]
		return addArrays2 ( firstArray, secondArray, array )

	elif ( allAreSame ( array1, array2, array3 ) ):
		return [ array1 ]



def userInterface ( root ):

	if ( input_check ( root ) ):
		return BSTSequences ( root )

	else:
		print ( "Invalid Input" )
		return
