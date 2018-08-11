"""
when n = 0:
possibleWays = 1

when n = 1:
possibleWays = 1

when n = 2:
possibleWays = 2

when n = 3:
possibleWays = 4

when n = 4:
possibleWays = 7

if n < 0, return 0
if n == 0, return 1
"""

def numOfWays ( n ):

	if ( inputIsValid ( n ) ):
		return numOfWaysHelper ( n )
	else:
		print ( "Invalid Input" )
		return

def numOfWaysHelper ( n ):

	if ( n < 0 ):
            return 0

        elif ( n == 0 ):
            return 1

        else:
            return numOfWaysHelper ( n - 1 ) + numOfWaysHelper ( n - 2 ) + numOfWaysHelper ( n - 3 )




def numOfWays ( n ):

	if ( inputIsValid ( n ) ):
		memo = [ None ] * n
		return numOfWaysHelper ( n, memo )
	else:
		print ( "Invalid Input" )
		return

def numOfWaysHelper ( n, memo ):

	if ( n == 0 ):
		memo [ n ] = 1
		return memo [ n ]

	elif ( n == 1 ):
		memo [ n ] = 1
		return memo [ n ]

	elif ( n == 2 ):
		memo [ n ] = 2
		return memo [ n ]

	if ( memo [ n - 1 ] is None ):
		memo [ n - 1 ] = numOfWaysHelper ( n - 1, memo )

	if ( memo [ n - 2 ] is None ):
		memo [ n - 2 ] = numOfWaysHelper ( n - 2, memo )

	if ( memo [ n - 3 ] is None ):
		memo [ n - 3 ] = numOfWaysHelper ( n - 3, memo )

	return memo [ n - 1 ] + memo [ n - 2 ] + memo [ n - 3 ]










