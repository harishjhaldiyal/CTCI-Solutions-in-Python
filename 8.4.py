"""
set = [ 2, 3 ]

power set = [ [ 2 ], [ 3 ], [ 2, 3 ], [ ] ]

a, b

power set = [ [ a ], [ b ], [ a, b ], [ ] ]

a,b,c

power set = [ [ a ], [ b ], [ c ], [ a, b ], [ a, c ], [ b, c ], [ a, b, c ], null ]

base case:

set = [ ]
powerset = [ [ ] ]

set = [ a ]
copyPowerSet = [ [ a ] ]

powerset = [ [ ], [ a ] ]

set = [ a, b ]

powerset = [ [ ], [ a ], [ b ], [ a, b ] ]

PseudoCode:

1) Create a powerset = [ [ ] ]
2) Traverse through the input set. For each element e in the input set:

a) copyPowerSet = powerset [ : ]
b) for each subset within copyPowerSet, append e to it and then append this subset to the powerset
"""

# Code:





def userInterface ( S ):

	if ( input_check ( S ) ):
		return powerSet ( S )

	else:
		print ( "Invalid Input" )
		return

def powerSet ( S ):

	powerset = [ [ ] ]
	for e in S:
		copyPowerSet = powerset [ : ] # [ [ ], [ a ] ]
		for subset in copyPowerSet: # [ a ]
			subset.append ( e ) # [ a, b ]
			powerset.append ( subset ) # [ [ ], [ a ], [ b ], [ a, b ] ]
	return powerset

"""
Time and space complexity: O ( n * ( 2 ^ n ) )
"""
		
