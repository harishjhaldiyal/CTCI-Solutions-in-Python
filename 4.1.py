"""
graph: a -> b -> c -> d

inputs: 

answer: b -> c -> d

bfs:      1) search 'd' into all the neighbors of node 'b'

	2) search 'd' into all the neighbors of the neighbors of 'b' one by one

Best conceivable runtime: O ( n )

Time complexity: O ( n )
Space complexity: O ( n ) - because of the 'state' attribute assuming that we have added it
"""

def search ( graph, start, end ):

	if ( start == end ):
		return True

	q = LinkedList ( )

	for i in graph.getNodes ( ):
		i.state = 'unvisited'

	start.state = 'visiting'

	q.add ( start )

	while ( not q.isEmpty ( ) ):
		u = q.removeHead ( )
		if ( u is not None ):
			for v in u.getAdjacent ( ):
				if ( v.state == 'unvisited' ):
					if ( v == end ):
						return True
					else:
						v.state = 'visiting'
						q.add ( v )
		u.state = 'visited'
	return False
