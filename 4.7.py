"""
projects: [ a, b, c, d, e, f ]

dependencies: [ [a, d], [f, b], [b, d], [f, a], [d, c] ]

order: f, a, d, b, d, c, e

projects with no dependency: e, f

graph:

		f					e

	b		a

		d
	
		c

build order: [ f, e ]

examples:
Case1:
projects = [ ]
dependencies = [ ]

Case2:
projects = [ a, b ]
dependencies = [ [ a, b ] ]

Time complexity: O ( D + P + P ) = O ( D + P )    -> P is the number of projects, D is the number of dependencies
Space complexity: O ( P + D )


"""

class Project ( object ):

	def __init__ ( self, name ):

		self.name = name
		self.children = [ ]
		self.incomingEdges = 0

	def addChild ( self, node ):

		self.children.append ( node.getName ( ) )
		node.incrementIncomingEdges ( )
		
	def incrementIncomingEdges ( self ):

		self.incomingEdges += 1

	def decrementIncomingEdges ( self ):

		self.incomingEdges -= 1

	def getName ( self ):

		return self.name

	def getChildren ( self ):

		return self.children

	def getIncomingEdges ( self ):

		return self.incomingEdges


class Graph ( object ):

	def __init__ ( self ):

		self.nodes = [ ]
		self.hashMap = { }

	def createNode ( self, n ):

		if ( n not in self.hashMap ):
                    node = Project ( n )
                    self.nodes.append ( node )
                    self.hashMap [ node.getName ( ) ] = [ ]

	def addEdge ( self, nodeParent, nodeChild ):

		if ( nodeParent in self.hashMap and nodeChild in self.hashMap ):

			self.hashMap [ nodeParent.getName ( ) ].append ( nodeChild )
			nodeParent.addChild ( nodeChild )

	def getNodes ( self ):

		return self.nodes


def buildGraph ( dependencies ):

	graph = Graph ( )

	for pair in dependencies:
		child = pair [ 0 ]
		parent = pair [ 1 ]
		graph.createNode ( parent )
		graph.createNode ( child )
		graph.addEdge ( parent, child )

	return graph

def process ( dependencies ):

	graph = buildGraph ( dependencies )
	buildOrder = [ ]
	nodes = graph.getNodes ( )
	for n in nodes:
		if ( n.getIncomingEdges ( ) == 0 ):
			buildOrder.append ( n )

	for e in buildOrder:
		children = e.getChildren ( )
		for c in children:
			c.decrementIncomingEdges ( )
			if ( c.getIncomingEdges ( ) == 0 ):
				buildOrder.append ( n )

	return buildOrder

def userInterface ( projects, dependencies ):

	if ( input_check ( projects, dependencies ) ):

		return process ( dependencies )
	
	else:

		print ( "Invalid Input" )
		return
			





