"""

naive approach - brute force

"""


def BalancedBT ( root ):

	if ( input_check ( root ) ):
		return process ( root )

	else:
		print ( "Invalid Input" )
		return

def isBalanced ( root ):

	if ( root is None ):
		return True

	leftHeight = getHeight ( root.left )
	rightHeight = getHeight ( root.right )
	heightDifference = abs ( leftHeight - rightHeight )
	
	if ( heightDifference > 1 ):
		return False

	else:
		return process ( root.left ) and process ( root.right )

def getHeight ( node ):

	if ( node is None ):
		return -1

	else:
		return max ( getHeight ( node.left ), getHeight ( node.right ) ) + 1



"""

recommended approach

"""


def checkHeight ( root ):

	if ( root is None ):
		return -1

	leftHeight = checkHeight ( root.left )
	if ( leftHeight == 'error' ):
		return 'error'

	rightHeight = checkHeight ( root.right )
	if ( rightHeight == 'error' ):
		return 'error'

	heightDifference = leftHeight - rightHeight
	if ( abs ( heightDifference ) > 1 ):
		return 'error'
	else:
		return max ( leftHeight, rightHeight ) + 1


def BalancedBT ( root ):

	if ( input_check ( root ) ):
		check = checkHeight ( root )
		if ( check == 'error' ):
			print ( "Tree not balanced" )
			return False

		else:
			return True

	else:
		print ( "Invalid Input" )
		return



	

