"""
array = [ 1,2,3,4,5,6,7,8,9 ]

stack1 = ( 1,2,3 )

size provided by user - calculate the size of the array: 3*size - get the top index for every stack

size of the array = n
stack1 = [ 0, n/3 )
stack2 = [ n/3 , 2n/3 )
stack3 = [ 2n/3, n )

push, pop, peek - user has to provide the stack number
isFull ( stackNumber ), isEmpty ( stackNumber ), getTop ( stackNumber )

Examples:

stackSize = 1

array = [ 0,0,0 ]

size = [ 0,0,0 ]
"""


class threeStacks ( object ):

	def __init__ ( self, stackSize ):

		self.stackSize = stackSize
		self.array = [ 0 ] * 3 * stackSize
		self.size = [ 0 ] * 3

	def getTop ( self, stackNumber, n = 3 * self.stackSize ):

		if ( stackNumber == 1 ):
			return 0

		elif ( stackNumber == 2 ):
			return int( n / 3 )

		elif ( stackNumber == 3 ):
			return int( 2 * ( n / 3 ) )

	def isFull ( self, stackNumber ):

		if ( self.size [ stackNumber - 1 ] == self.stackSize ):
			return True
		else:
			return False



	def isEmpty ( self, stackNumber ):
	
		if ( self.size [ stackNumber - 1 ] == 0 ):
			return True
		else:
			return False


	def push ( self, element, stackNumber ): # 5 to 2nd stack

		if ( self.isFull ( stackNumber ) ):
			raise Exception ( "The stack is full" )
		else:
			top = self.getTop ( stackNumber )
			self.array [ top ] = element
			self.size [ stackNumber - 1 ] += 1

	def pop ( self, stackNumber ):

		if ( self.isEmpty ( stackNumber ) ):
			raise Exception ( "The stack is empty" )

		else:
			top = self.getTop ( stackNumber )
			value = self.array [ top ]
			self.array [ top ] = 0
			self.size [ stackNumber - 1 ] -= 1
			return value

	def peek ( self, stackNumber ):

		if ( self.isEmpty ( stackNumber ) ):
			raise Exception ( "The stack is empty" )

		else:
                        top = self.getTop ( stackNumber )
                        return self.array [ top ]
		

		



