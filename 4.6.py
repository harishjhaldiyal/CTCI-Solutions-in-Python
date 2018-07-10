"""
					6

			3					9

		2		4		7				15
							
									11			18
								
								10		13	17	       19

input = 9

n nodes
Time complexity: O ( log n )
Space complexity: O ( log n )
"""

def inorder ( root ):

	while ( root is not None ):
            result = root
            root = root.left
        return result	


def successor1 ( node ):

	if ( node.right is not None ):
		return inorder ( node.right, None )

	else:
		return successor2 ( node )















def successor2 ( node ):	

	if ( node.parent is not None ):
            parent = node.parent
            if ( parent.left is not None ):
                if ( node == parent.left ):
                    return parent

            if ( parent.right is not None ):
                if ( node == parent.right ):
                    return successor2 ( parent )

        else:
            print ( "There is no successor" )
            return



def userInterface ( node ):

	if ( input_check ( node ) ):
		return successor1 ( node )

	else:
		print ( "Invalid Input" )
		return
