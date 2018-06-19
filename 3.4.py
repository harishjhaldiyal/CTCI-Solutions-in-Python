"""
queue = ( 1,2,3,4,5,6 ) - FIFO

stack1 = (  ) - LIFO

stack2 = (  )

insertion = 1,2,3,4,5,6
pop = 1,2,3,4,5,6

n elements in stack1

Time complexity of each operation: O ( n )
Space complexity: O ( 1 ) / O ( n ) - if stack1 or stack2 are considered extra space

size of the stack = k = 5
"""


class Queue ( object ):

	def __init__ ( self, size ):

		self.size = size
		self.stack1 = Stack ( )
		self.stack2 = Stack ( )


	def getSize ( self ):

		return ( self.stack1.getLength + self.stack2.getLength )

	def push ( self, element ):

		if ( self.getSize ( ) < self.size ):

                    self.stack1.push ( element )

                else:
                
               	    raise Exception ( "The queue is full" )





	def pop ( self ):

		if ( self.stack2.getLength > 0 ):

                    self.stack2.pop ( )

                else:
                
                   if ( self.stack1.getLength > 0 ):
                   	while ( self.stack1.getLength > 0 ):
                   	    element = self.stack1.pop ( )
                   	    self.stack2.push ( element )
                    
                        self.stack2.pop ( )
                
             	  else:
                
                	raise Exception ( "The queue is empty" )
