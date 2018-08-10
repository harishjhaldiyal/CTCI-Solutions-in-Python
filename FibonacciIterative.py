"""

series = 0, 1, 1, 2, 3, 5, ...

first fib = 0
second fib = 1
third fib = first fib + second fib


"""

def fib ( n ):

	if ( input_check ( n ) ):
            memo = [ None ] * ( n + 1 )
            return fibHelperIterative ( n, memo )
        else:
            print ( "Invalid Input" )
            return


def fibHelperIterative ( n, memo ):

	memo [ 1 ] = 0
	memo [ 2 ] = 1
	
	for i in range ( 3, n + 1 ):
		memo [ i ] = memo [ i - 1 ] + memo [ i - 2 ]

	return memo [ n ]


def fibHelperIterativeAdvanced ( n ):

	firstNum = 0
	secondNum = 1
	
	for i in range ( 3, n + 1 ):
		i_thFib = firstNum + secondNum
		firstNum = secondNum
		secondNum = i_thFib
	return i_thFib

