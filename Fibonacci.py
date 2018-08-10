"""

series = 0, 1, 1, 2, 3, 5, ...

first fib = 0
second fib = 1
third fib = first fib + second fib


"""

def fib ( n ):

	if ( input_check ( n ) ):
            memo = [ None ] * ( n + 1 )
            return fibHelper ( n, memo )
        else:
            print ( "Invalid Input" )
            return


def fibHelper ( n, memo ):

	if ( n == 1 ):
		memo [ n ] = 0
		return memo [ n ]

	elif ( n == 2 ):
		memo [ n ] = 1
		return memo [ n ]

	else:
		if ( memo [ n - 1 ] is None ):
			memo [ n - 1 ] = fib ( n - 1, memo )
		if ( memo [ n - 2 ] is None ):
			memo [ n - 2 ] = fib ( n - 2, memo )
		return memo [ n - 1 ] + memo [ n - 2 ]

