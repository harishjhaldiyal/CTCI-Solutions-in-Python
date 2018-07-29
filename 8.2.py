"""
grid = 2D array

r rows, c columns

grid:

[
 
[ 1, 0, 0, 0 ]
[ 0, 0, 0, 0 ]
[ 0, -1, 0, 0 ]
[ 0, 0, 0, 0 ]

]

initial point = grid [ 0 ] [ 0 ]
final point = grid [ r - 1 ] [ c - 1 ]

one step before = grid [ r - 2 ] [ c - 1 ] or grid [ r - 1 ] [ c - 2 ]

one more step backwards for grid [ r - 2 ] [ c - 1 ]:
grid [ r - 3 ] [ c - 1 ] or grid [ r - 2 ] [ c - 2 ]

one more step backwards for grid [ r - 1 ] [ c - 2 ]:
grid [ r - 2 ] [ c - 2 ] or grid [ r - 1 ] [ c - 3 ]

recursive case:
grid [ r - 1] [ c - 1 ] = grid [ r - 2 ] [ c - 1 ] + grid [ r - 1 ] [ c - 2 ]

"""












def pathTillPosition ( grid, r , c, path, obstacleCells ):

	if ( r < 0 or c < 0 or not grid [ r ] [ c ] ):
		return False

	isAtOrigin = ( r == 0 ) and ( c == 0 )

	point = [ r, c ]
	if ( point in obstacleCells ):
		return False

	if ( isAtOrigin or pathTillPosition ( grid, r - 1, c, path ) or pathTillPosition ( grid, r , c - 1, path ) ) :
		path.append ( point )
		return True

	obstacleCells.add ( point )
	return False


def userInterface ( grid ):

	if ( input_check ( grid ) ):
		obstacleCells = set ( )
		path = [ ]
		if ( pathTillPosition ( grid, len ( grid ) - 1 , len ( grid [ 0 ] ) - 1, path, obstacleCells ) ):
			return path

		else:
			print ( "Path not possible" )
			return

	else:
		print ( "Invalid Input" )
		return

