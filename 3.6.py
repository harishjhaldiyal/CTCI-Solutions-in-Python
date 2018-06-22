"""
number of animals = n

queueDog = d-> d-> d -> d -> x

queueCat = c -> c -> x


Space complexity: O ( n )
Time complexity: O ( 1 )
"""

class AnimalShelter ( object ):

	def __init__ ( self, size ):

		self.size = size
		self.queueDog = LinkedList ( )
		self.queueCat = LinkedList ( )
		self.order = 0

	def enqueue ( self, animal ):

		if ( self.queueDog.size ( ) + self.queueCat.size ( ) < self.size ):

                            if ( animal.type == 'dog' ):
                               	self.order += 1
                               	animal.order = self.order
                           	self.queueDog.add ( animal )
                           	return
                                
                            elif ( animal.type == 'cat' ):
                           	self.order += 1
                               	animal.order = self.order
                           	self.queueCat.add ( animal )
                           	return
                                
                            else:
                           	raise Exception ( "Invalid Input" )
                    
                else:
                    
                            raise Exception ( "The shelter is full" )



        def removeDog ( self ):
        
               	if ( self.queueDog.size ( ) != 0 ):
                
                    self.queueDog.removeHead ( )
                    return
                
                else:
                
               	    raise Exception ( "There is no dog in the shelter" )






        def removeCat ( self ):
        
               	if ( self.queueCat.size ( ) != 0 ):
                
                    self.queueCat.removeHead ( )
                    return
                
                
                else:
                
               	    raise Exception ( "There is no cat in the shelter" )



	def removeAny ( self ):

		if ( self.queueDog.size ( ) > 0 and self.queueCat.size ( ) > 0 ):

                    headDog = self.queueDog.head ( )
                    headCat = self.queueCat.head ( )
                    if ( headDog.order < headCat.order ):
                   	self.queueDog.removeHead ( )
                   	return
                    else:
                   	self.queueCat.removeHead ( )
                   	return

                elif ( self.queueDog.size ( ) > 0 ):
                       	self.queueDog.removeHead ( )
                        return
                
                
                elif ( self.queueCat.size ( ) > 0 ):
                       	self.queueCat.removeHead ( )
                        return
                
                
                else:
               	        raise Exception ( "The shelter is empty" )

	





class Animal ( object ):

	def __init__ ( self, type ):

		self.type = type
		self.order = None


"""
Test:
d1 = Animal ( dog )
c1 = Animal ( cat )
d2 = Animal ( dog )

d2 - order = 1
c1 - order = 2
d1 - order = 3
"""