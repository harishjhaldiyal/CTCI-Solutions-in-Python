"""
grid 1:
[
 [ 1, 2 ],
 [ None, 3 ]
]

grid 2:
[
 [ 1, 2, 3, 4 ],
 [ None, 5, 6, 7 ],
[ 8, 9, 10, 11 ],
[ 12, 13, 14, 15 ]
]

grid 3:

[
 [ 1 ]
]

grid 4:

[
 [ 1, 2 ]
]

grid 5:

[
 [ 1, 2, 3 ]
]

grid 6:

[
 [ 1, 2 ],
 [ 3, 4 ]
]


"""






"""
Pseudocode:

path = [ ]

1. If the current point is out of bound of the grid or current point is None, then return False

2. Else, add the current point to the path

3. Repeat the same process for ( next element in the row or next element in the column )

"""

#Time complexity: 2 ^ ( n.o of rows + n.o of cols )
#Space complexity: n.o of rows + n.o of cols

#Code

def robotInGrid ( grid ):

	if ( isValid ( grid ) ):
		numberOfRows = len ( grid )
		numberOfCols = len ( grid [ 0 ] )
		path = [ ]
		if ( robotInGridHelper ( grid, path, numberOfRows, numberOfCols, 0, 0 ) ):
			return path.reverse ( )
		else:
			print ( "No path exist" )
			return

	else:
		print ( "Invalid Input" )
		return













def robotInGridHelper ( grid, path, numberOfRows, numberOfCols, firstIndex, secondIndex ):

	if ( ( secondIndex > numberOfCols - 1 ) or ( firstIndex  > numberOfRows - 1 ) ):
		return False

	currentCell = grid [ firstIndex ] [ secondIndex ]
	if ( currentCell is None ):
		return False
		
        currentPoint = [ firstIndex, secondIndex ]
	
	target = grid [ numberOfRows - 1 ] [ numberOfCols - 1 ]

	if ( currentCell == target ):
		return True

	if ( ( robotInGridHelper ( grid, path, numberOfRows, numberOfCols, firstIndex, secondIndex + 1 ) ) or  ( robotInGridHelper ( grid, path, numberOfRows, numberOfCols, firstIndex + 1, secondIndex ) ) ):
		"""
		Note that the 'or' operator supports short circuiting: if the first part of the 'or' is true, then the process will not evaluate the second part, and therefore, only one path will be there from starting to end.
		"""
		path.append ( currentPoint )
                return True

        else:
                return False









def robotInGridHelper2 ( grid, path, numberOfRows, numberOfCols, firstIndex, secondIndex, falseHashSet ):

	if ( ( secondIndex > numberOfCols - 1 ) or ( firstIndex  > numberOfRows - 1 ) ):
		return False

	currentPoint = [ firstIndex, secondIndex ]
	if ( currentPoint in falseHashSet ):
		return False

        currentCell = grid [ firstIndex ] [ secondIndex ]
	if ( currentCell is None ):
		return False
	
	target = grid [ numberOfRows - 1 ] [ numberOfCols - 1 ]

	if ( currentCell == target ):
		return True

	if ( ( robotInGridHelper ( grid, path, numberOfRows, numberOfCols, firstIndex, secondIndex + 1, falseHashSet ) ) or  ( robotInGridHelper ( grid, path, numberOfRows, numberOfCols, firstIndex + 1, secondIndex, falseHashSet ) ) ):
		"""
		Note that the 'or' operator supports short circuiting: if the first part of the 'or' is true, then the process will not evaluate the second part, and therefore, only one path will be there from starting to end.
		"""
		path.append ( currentPoint )
                return True

        else:
                falseHashSet.add ( currentPoint )
                return False



