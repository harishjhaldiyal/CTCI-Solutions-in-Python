"""
countWays ( n ) = countWays ( n - 1 ) + countWays ( n - 2 )  + countWays ( n - 3 )

steps = 4
number of ways = 6

1,1,1,1
1,1,2
1,2,1
2,1,1
1,3
3,1

countWays ( 4 ) = countWays ( 3 ) + countWays ( 2 )  + countWays ( 1 )

1,1,1
1,2
2,1
3


countWays ( 1 ) = 1
countWays ( 0 ) = 1
countWays ( 2 ) = 1

countWays ( 3 ) = countWays ( 2 ) + countWays ( 1 )  + countWays ( 0 )

countWays ( 0 ) = countWays ( -1 ) + countWays ( -2 )  + countWays ( -3 )

if ( n < 0 ):
	return 0

if ( n == 0 ):
	return 1



countWays ( 1 ) = countWays ( 0 ) + countWays ( -1 )  + countWays ( -2 )

countWays ( 2 ) = countWays ( 1 ) + countWays ( 0 )  + countWays ( -1 )

countWays ( 3 ) = countWays ( 2 ) + countWays ( 1 )  + countWays ( 0 )

Memo array will take O(n) space. So yes again, the SPACE is O(n + n) = O(n).
"""


#code:

def countWays ( n, memo ):

	if ( n < 0 ):
		return 0

	if ( n == 0 ):
		return 1

	if ( memo [ n ] is not None ):
		return memo [ n ]

	memo [ n ] = countWays ( n - 1 ) + countWays ( n - 2 ) + countWays ( n - 3 )
	return memo [ n ]

def userInterface ( n ):

	if ( input_check ( n ) ):
		memo = [ None ] * n
		return countWays ( n, memo )

	else:
		print ( "Invalid input" )
		return


















