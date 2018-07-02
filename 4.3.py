"""
					6			
			4				8
		3		5		7		9

"""

def LinkedListNodes ( root ):

	if ( input_check ( root ) ):
		return BFS ( root )
	else:
		print ( "Invalid Input" )
		return


def BFS ( root ):

	linkedListArray = [ ]
        queue = Queue ( )
	root.marked = true
	queue.enqueue ( root )
	nodesinNextLevel = 1

	while ( queue.size ( ) > 0 ):
		nodesinCurrentLevel = nodesinNextLevel
		nodesinNextLevel = 0
		ll = LinkedList ( )

		i = 1
		while ( i <= nodesinCurrentLevel ):
                    node = queue.dequeue ( )
                    ll.add ( node )
                    for e in node.adjacent:
                            if not e.marked:
                                    e.marked = True
                                    queue.enqueue ( e )
                                    nodesinNextLevel += 1
                    i += 1

                linkedListArray.append ( ll.head ( ) )

        return linkedListArray
	



