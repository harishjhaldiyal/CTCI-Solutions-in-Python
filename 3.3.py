"""
stack1 = [ 1,2,3 ]
stack2 = [ 4,5,6 ]
[ [ 1,2,3 ], [ 4,5,6 ] ]
[ stack1, stack2 ]

examples:

stacksSet = [ stack1 ]

stack1 = [ 1,2,3 ]
"""


class SetOfStacks ( object ):

	def __init__ ( self, size ):

		self.size = size
		self.stacksSet = [ ]

	def push ( self, element ):
	
		if ( len ( self.stacksSet ) == 0 ):
			stack = Stack ( )
			self.stacksSet.append ( stack )

		latestStack = self.stacksSet [ -1 ]

		if ( latestStack.getLength == self.size ):

			newstack = Stack ( )
			self.stacksSet.append ( newstack )
			latestStack = self.stacksSet [ -1 ]

		latestStack.push ( element )


	def pop ( self ):

		if ( len ( self.stacksSet ) > 0 ):
                    latestStack = self.stacksSet [ -1 ]
      		    value = latestStack.pop ( )
      		    if ( latestStack.getLength == 0 ):
     			del self.stacksSet [ -1 ]
      		    return value

	       else:
		  raise Exception ( ' The Stack Set is Empty ' )






        def popAt ( self, ind ):
        
                if ( ind < len ( self.stacksSet ) ):
                
                        getStack = self.stacksSet [ ind ]
                       	return getStack.pop ( )
                
                else:
                
               	        raise Exception ( ' Error ' )



		
