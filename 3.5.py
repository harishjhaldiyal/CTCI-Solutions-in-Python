"""
stack = ( 10,7,6,4 )

size = 4

top = 4

temp_variable = 7

temp_stack = (  )

Time complexity: O ( n ( n + n ) ) = O ( n^2 )

Space complexity: O ( n )
"""



class MinStack ( object ):

	def __init__ ( self, size ):

		self.size = size
		self.stack = Stack ( self.size )
		self.temp_stack = Stack ( self.size )
		self.temp_variable = None
		self.top = None

	def push ( self, element ):

		if ( self.stack.getSize < self.size ):
		      self.stack.push ( element )

          	      if ( self.top is None ):
         			self.top = self.stack.peek ( )
            
          	      else:
         			if ( self.stack.peek ( ) > self.top ):
            				self.temp_variable = self.stack.pop ( )
            				          				          				
            
                                        while ( self.stack.peek ( ) < self.temp_variable ):
          					e = self.stack.pop ( )
          					self.temp_stack.push ( e )
            
            				self.stack.push ( self.temp_variable )
            
            				while ( self.temp_stack.getSize > 0 ):
          					self.stack.push ( self.temp_stack.pop ( ) )
         			else:
            				self.top = self.stack.peek ( )

	        else:
                    raise Exception ( "The stack is full")
			
			
			



