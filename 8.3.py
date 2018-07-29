"""
sorted distinct elements
A [ i ] = i

A = [ 5 ,5 ,2 ]
approach 1: just traverse through the array and compare the current index with the value at that index
time = O ( n )
space = O ( 1 )

A = [ 0, 1, 5 ]

A = [ 5, 6, .. ]


A = [ -6, -5, 2, 6, 8, 10 ]

          0, 1, 2, 3, 4,  5
"""

def userInterface ( A ):

	if ( input_check ( A ) ):
		return magicIndex ( A )

	else:
		print ( "Invalid Input" )
		return

def magicIndex ( A ):

	start = 0
	end = int ( len ( A ) - 1 )
	
	while ( start < end ):
		middleIndex = int ( ( start + end ) / 2 )
		middleValue = A [ middleIndex ]

		if ( middleValue > middleIndex ):
			end = middleIndex - 1

		elif ( middleValue < middleIndex ):
			start = middleIndex + 1

		elif ( middleValue == middleIndex ):
			return middleIndex

	return


"""
A = [ 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8 ]

        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


A = [ 1, 5, 5, 5, 5, 7, 7, 7, 9, 10, 11 ]

        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for left search = start to min ( middleValue, middleIndex - 1 )
for right search = max ( middleValue, middleIndex + 1 ) to end
"""

def magicIndex2 ( A, start, end ):

	if ( start > end ):
		return -1

	middleIndex = int ( ( start + end ) / 2 )
	middeValue = A [ middleIndex ]
	if ( middleIndex == middeValue ):
		return middleIndex

	leftMaxValue = min ( middleValue, middleIndex - 1 )
	leftSearch = magicIndex2 ( A, start, leftMaxValue ):
	if ( leftSearch >= 0 ):
		return leftSearch

	rightMinValue = max ( middleValue, middleIndex + 1 )
	rightSearch = magicIndex2 ( A, rightMinValue , end )
	return rightSearch





