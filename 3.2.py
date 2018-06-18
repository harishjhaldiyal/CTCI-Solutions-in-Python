"""
We may also implement this solution with LinkedList as Stack. If we kept track of the minimum at each state, we would be able to easily know the minimum. We can do
this by having each node record what the minimum beneath itself is ( and also one record in the 'LinkedList' class that would store the global minimum ):
class Node ( object ):
    
    def __init__ ( self, value ):
        
        self.minimumUntilNow = None
        
class LinedList ( object ):
    
    def __init__ ( self ):
        
        self.globalMinimum = None
        
    def setGlobalMinimum ( self ):
        
        if ( node.data < self.globalMinimum ):
            self.globalMinimum = node.data
            node.minimumUntilNow = node.data
            
        else:
            node.minimumUntilNow = self.globalMinimum
      
"""


"""
stack = ( 1,2,3,4,5,6 )
push, pop, min - O(1)
stack = ( 1,2,3,4,5,6,0 )
min = 0
1. push:
2. pop
3. min
examples:
size = 5
stack = [ 10, 5, 6 ]
min = [ 10, 5, 5 ]
"""

class minStack ( object ):

	def __init__ ( self, size ):
		
		self.size = size
		self.stack = [ ]
		self.min = [ ]

	def push ( self, element ):
		
		if ( self.isFull ( ) ):
			raise Exception ('The stack is already full')

		else:
			if ( self.length == 0 ):
				self.min.append ( element )

			else:
				if ( element < self.min [ -1 ] ):
					self.min.append ( element )
				
				else:
					value = self.min [ -1 ]
					self.min.append ( value )
			self.stack.append ( element )

	def pop ( self ):

		if ( self.isEmpty ( ) ):
			raise Exception ('The stack is empty')
		
		else:
			value = self.stack [ -1 ]
			del self.stack [ -1 ]
			del self.min [ -1 ]
			return value


	def min ( self ):

		
		if ( self.isEmpty ( ) ):
			raise Exception ('The stack is empty')
		
		else:
			return self.min [ -1 ]


	def isFull ( self ):

		if ( len ( self.stack ) == self.size ):
			return True

		else:
			return False
		

	def isEmpty ( self ):

		if ( len ( self.stack ) == 0 ):
			return True

		else:
			return False